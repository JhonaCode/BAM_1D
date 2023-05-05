#)!/bin/bash 
#help#
#****************************************************************************#
# Script to run agcm 1D, version 4.0.0 model on CRAY.
#
# usage: run_bam CaseName
# CaseName: Experiment name which is linked
#           to a directory containing initial condition, sonding profile 
#           (SOND_IN) and boundary condition(s) (FORCINGS_ASCII or FORCING_IN).
#           FORCINGS_ASCII contains a time series of tendencies profiles
#           FORCING_IN contains a tendency profile, that is kept constant
#           for the integration.
#           Always:
#           Although in CaseName some configurations of files like
#           VegetationMask, DeepSoilTemperature and others are done. It
#           is convenient to review them.
#
# Enver Ramirez
#****************************************************************************#
#****************************************************************************#
#CALLING SEQUENCE:
#      
#      ./runModel <opções>
#
#         As <opções> válidas são:
#            * -t <val> : truncamento [default: 62]
#            * -l <val> : numero de niveis [default: 28]
#            * -p <val> : prefixo dos arquivos do BAM (condição inicial e previsões) [default: NMC]
#            * -np <val>: numero de processadores [default: 72]
#            * -N <val> : numero de nós [default: 24]
#            * -d <val> : numero de Treads por processos MPI [default: 1]
#            * -I <val> : Data da condição inicial [defaul, in the begining of the runModel.sh] 
#            * -F <val> : Data da previsão final   [defaul, in the begining of the runModel.sh] 
#            * -W <val> : Data da condição inicial (Warm start) [defaul, in the begining of the runModel.sh] 
#            * -i <val> : Tipo de Inicialização [default: 2]
#            * -s <val> : Arquivo de SST [default: sstwkl]
#            * -ts <val>: TimeStep da previsão [default: 6]
#            * -r <val> : Generate Restart Files [default: .FALSE.]
#            * -tr <val>: TimeStep do Restart  [default: 6]

# Jhonatan Aguirre  
#****************************************************************************#
#
#  example:
#
#     ./runModel -t 62 -l 28 -I 2013010100 -F 2013010118
#
# !REVISION HISTORY:
#    15-01-2020 -Jhonatan Aguirre- PARMODEL DATAS in runModel 
#help#
#
export HOME1=`pwd`

#Input and Output directories
#dirbase=$(dirname "`pwd`")

DataIn=${HOME1}/../model/datain/
DataOut=${HOME1}/../model/dataout/

#python options 
#Jhonatan
fpython=${HOME1}/../python/


#Exp is the only mandatory variable. Experiment name and ensemble length is related to this variable
Exp=(IOP2)

path=`pwd`

#To subtract '/run' from path
path2=`echo ${path} | awk '{print substr($1,1,index($1,"/run")-1)}'`


#If the dates are not passed  by the coman line, they are defined as:
# modify to be optional arguments
# For each data between ${s} and ${e} (inclusive) BAM is run for a short ${sprint} sprint
#For definition go to line
# initial date
s="00z15Feb2014"  
## end date
e="00z15May2014"  
##sprint="+3 days"  # sprint


#Checking arguments
if [ "${1}" = "help" -o -z "${1}" ]
then
  cat < ${0} | sed -n '/^#help#/,/^#help#/p'
  echo "The defaul exp GAN is used in the defaul period"
  echo "    "$DataIn
fi


#$( ) runs shell commands.
#$(( )) evaluates arithmetic expressions.

# Pegando as opções que foram passadas pela linha de comando

POSITIONAL=()
while [[ $# -gt 0 ]]; do
  key="$1"

  case $key in

      -exp|--experiment)
      EXPE="$2"
      shift # past argument
      shift # past value
      ;;

      -t|--Trunct)
      TRC="$2"
      shift # past argument
      shift # past value
      ;;

      -l|--levels)
      LV="$2"
      shift # past argument
      shift # past value
      ;;

      -dt|--time_step)
      TIMESTEP="$2"
      shift # past argument
      shift # past value
      ;;

      -I|--timei )
      LABELI="$2"
      shift # past argument
      shift # past value
      ;;

      -W|--timew )
      LABELW="$2"
      shift # past argument
      shift # past value
      ;;

      -F|--timef )
      LABELF="$2"
      shift # past argument
      shift # past value
      ;;

      -s|--xxx )
      NST="$2"
      shift # past argument
      shift # past value
      ;;

      -ts|--xxx )
      DHT="$2"
      shift # past argument
      shift # past value
      ;;

      -h|--xxx )
      DHS="$2"
      shift # past argument
      shift # past value
      ;;

      -dn|--xxx )
      DHN="$2"
      shift # past argument
      shift # past value
      ;;

      -nh|--xxx )
      NHN="$2"
      shift # past argument
      shift # past value
      ;;

      *)    # unknown option  
      POSITIONAL+=("$1") # save it in an array for later
      shift # past argument
      ;;
  esac
done

#Ensemble of Physics
ILCON=(HUMO)   #(UKMO HGFS MIC HUMO)  #  Opcoes de microfisicas
ICCON=(GRE)    #(GEC GRE RAS)         #  Opcoes de conveccao cumulus
ISWRAD=(CRD)   #(CRD CRD CRD)         #  Short wave radiation
ILWRAD=(RRTMG) #(RRTMG HRS HRS)       #  long wave radiation
schemes=(1 1 1 1)    #(3 3 3) 
Wgh1=(0. 0. 0. 0.)   #(0.0 0.0 0.0) 
Wgh2=(1. 1. 1. 1.)   #(0.0 0.0 0.0)
Wgh3=(0. 0. 0. 0.)   #(1.0 1.0 1.0) 
CRDCLD=(6 6 6 6)     #(1 1 1) 
slhum=(.TRUE. .TRUE. .TRUE. .TRUE.) #(.FALSE.)     #(.FALSE. .TRUE. .FALSE.)
microphys=(.TRUE. .TRUE. .TRUE. .TRUE.) #(.FALSE. .TRUE. .FALSE.)
forcings_weight_d=(1. 1. 1. 1.)         # test sensitivity of dynamics forcing
forcings_weight_t=(1. 1. 1. 1.)         # '                 ' temperature forcing
forcings_weight_m=(1. 1. 1. 1.)         # '                 ' moisture forcing


# Run with defaul experiment 
if [ -z ${EXPE} ];then
   #EXPE=GAN
   EXPE=GOA_IOP1_ir
fi

# truncamento
if [ -z ${TRC} ];then
   TRC=62
fi

# numero de niveis verticais
if [ -z ${LV} ];then
   LV=28
fi

# numero de niveis verticais
if [ -z ${DELT} ];then
   DELT=360
fi

#Data of the experiment
########################################################################
###s="00z01Oct2011"  
##### end date
###e="00z30Jan2012" 

# strip ${s} and ${e} in terms of Y(year), m(month), d(day) and H(hour)
if [ -z ${LABELI} ];then

	strip=(Y m d H)
	idx=0
	for x in "${strip[@]}"
	do
	   t0[idx]=$(date -u -d "${s} +0 days" "+%${x}")
	   tf[idx]=$(date -u -d "${e} +0 days" "+%${x}")
	   idx=`expr $idx + 1`
	done

	#Dates.
	LABELI="${t0[3]},${t0[2]},${t0[1]},${t0[0]}"
	LABELF="${tf[3]},${tf[2]},${tf[1]},${tf[0]}"
	LABELW=${LABELF}

    echo -e "\033[32;1m LABELI,LABELF and LABELW are not set. The defaul dates are used \033[m"
    echo -e "\033[32;1m LABELI ${LABELI} \033[m"
    echo -e "\033[32;1m LABELW ${LABELW} \033[m"
    echo -e "\033[32;1m LABELF ${LABELF} \033[m"

else
	strip=(Y m d H)
	idx=0
	for x in "${strip[@]}"
	do
	   t0[idx]=$(date -u -d "${LABELI} +0 days" "+%${x}")
	   tf[idx]=$(date -u -d "${LABELF} +0 days" "+%${x}")
	   idx=`expr $idx + 1`
	done
	LABELI="${t0[3]},${t0[2]},${t0[1]},${t0[0]}"
	LABELF="${tf[3]},${tf[2]},${tf[1]},${tf[0]}"
	LABELW=${LABELF}

fi


# Arquivo de SST
if [ -z ${NST} ];then
   NST=\'sstaoi\'
fi

# TimeStep da Previsão
# interval in hours to output diagnostics,      
# equal zero to use default list

if [ -z ${DHT} ];then
   DHT=1
fi

#interval in hours to output restart,          
#equal zero to use default list

if [ -z ${DHS} ];then
   DHS=48
fi
# TimeStep da Previsão
if [ -z ${DHN} ];then
   DHN=48
fi

#time in hours to stop DHN diagnostics,
#! equal zero to not execute DHN diagnostics
# TimeStep da Previsão
if [ -z ${NHN} ];then
   NHN=48
fi

#!#############################################################################
#!
#! trunc    =021,vert     =09,dt       =1800.0,
#! trunc    =062,vert     =28,dt       =1200.0,
#! trunc    =126,vert     =28,dt       =600.0
#! trunc    =170,vert     =42,dt       =450.0
#! trunc    =213,vert     =42,dt       =360.0
#! trunc    =254,vert     =64,dt       =300.0
#! trunc    =341,vert     =64,dt       =200.0  !!!teste=225.0
#!############################################################################

case ${TRC} in
    62)TimeStep=360;;
     *)echo -e "\033[32;1m Truncamento desconhecido ${TRC} \033[m"
esac

#################################
CaseName=${EXPE}

x=0
upx=${#Exp[@]}
while [ "$x" -lt "$upx" ]
do

#Check existence of output dir
dirfNameOutput=${DataOut}${Exp[x]}/

if [ -d "$dirfNameOutput" ]
then
    echo "directory $dirfNameOutput exist"
else
    mkdir $dirfNameOutput
fi


sed  -e "s;##TRUNC##;${TRC};g"\
     -e "s;##NLEV##;${LV};g"\
     -e "s;##DELT##;${TimeStep};g"\
     ${DataIn}${CaseName}/PARMODEL > ${path}/PARMODEL

#     -e "s;##LABELI##;${LABELI};g"\
#     -e "s;##LABELW##;${LABELW};g"\
#     -e "s;##LABELF##;${LABELF};g"\
#
#-e "s;#NST#;${NST};g" \
#-e "s;#DHT#;${DHT};g" \
#-e "s;#DHS#;${DHS};g" \
#-e "s;#DHN#;${DHN};g" \
#-e "s;#NHN#;${NHN};g" \

# copy CaseName data to datain (IC, BC, PARMODEL default)
if [ "$x" -eq "0" ]
then 
  echo "copy IC, BC, PARMODEL from "${CaseName}
  echo "cp "${DataIn}${CaseName}/*" "${DataIn}/
  echo "cp "${DataIn}${CaseName}/PARMODEL" "${path}/
  cp ${DataIn}${CaseName}/* ${DataIn}/
  cp ${path}/PARMODEL ${path}/
else
  echo "jumping copy" 
fi



#erg2015 cp ${path}/PARMODEL ${path2}/model/exec/
#erg2015 cp ${path}/SOND_IN ${path2}/model/datain/
#erg2015 cp ${path}/FORCINGS_ASCII ${path2}/model/datain/

#erg##########################################################
#cat ......
#erg##########################################################

cp ${path}/PARMODEL ${path}/parmodel_test
cp ${path}/PARMODEL ${path}/PARMODEL.BKP.ENVER
echo "cp "${path}/PARMODEL ${path}/parmodel_test
echo "cp "${path}/PARMODEL ${path}/PARMODEL.BKP.ENVER

echo ${Exp[x]}

 
aspa="'"
coma=","

cat ${path}/parmodel_test  | awk -v var="${DataIn}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,7) == "path_in" && var != ""  )
                           { print " "substr($1,1,7)" = "aspa var aspa coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${dirfNameOutput}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,14) == "dirfNameOutput" && var != ""  )
                           { print " "substr($1,1,14)" = "aspa var aspa coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${ICCON[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,5) == "ICCON" && var != ""  )
                           { printf(" ICCON = %s%s%s,      ! iccon=KUO:cumulus convection(kuo)\n",aspa,var,aspa) }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${ILCON[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,5) == "ILCON" && var != ""  )
                           { print " "substr($1,1,5)" = "aspa var aspa coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${ISCON[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,5) == "ISCON" && var != ""  )
                           { print " "substr($1,1,5)" = "aspa var aspa coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${ISWRAD[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,6) == "ISWRAD" && var != ""  )
                           { print " "substr($1,1,6)" = "aspa var aspa coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${ILWRAD[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,6) == "ILWRAD" && var != ""  )
                           { print " "substr($1,1,6)" = "aspa var aspa coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${ASOLC[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,5) == "ASOLC" && var != ""  )
                           { print " "substr($1,1,5)" = "var coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${ASOLM[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,5) == "ASOLM" && var != ""  )
                           { print " "substr($1,1,5)" = "var coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${grepar1[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,7) == "grepar1" && var != ""  )
                           { print " "substr($1,1,7)" = "var coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${grepar2[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,7) == "grepar2" && var != ""  )
                           { print " "substr($1,1,7)" = "var coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${grepar3[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,7) == "grepar3" && var != ""  )
                           { print " "substr($1,1,7)" = "var coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${atmpbl[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,6) == "atmpbl" && var != ""  )
                           { print " "substr($1,1,6)" = "var coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${CRDCLD[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,6) == "CRDCLD" && var != ""  )
                           { print " "substr($1,1,6)" = "var coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${PBLEntrain[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,10) == "PBLEntrain" && var != ""  )
                           { print " "substr($1,1,10)" = "aspa var aspa coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${schemes[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,7) == "schemes" && var != ""  )
                           { print " "substr($1,1,7)" = "var coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${OCFLUX[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,6) == "OCFLUX" && var != ""  )
                           { print " "substr($1,1,6)" = "aspa var aspa coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${SLABOCEAN[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,9) == "SLABOCEAN" && var != ""  )
                           { print " "substr($1,1,9)" = "aspa var aspa coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${ICEMODEL[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,8) == "ICEMODEL" && var != ""  )
                           { print " "substr($1,1,8)" = "aspa var aspa coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${omlmodel[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,8) == "omlmodel" && var != ""  )
                           { print " "substr($1,1,8)" = "aspa var aspa coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${oml_hml0[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,8) == "oml_hml0" && var != ""  )
                           { print " "substr($1,1,8)" = "var coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${Wgh1[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,4) == "Wgh1" && var != ""  )
                           { print " "substr($1,1,4)" = "var coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${Wgh2[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,4) == "Wgh2" && var != ""  )
                           { print " "substr($1,1,4)" = "var coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${Wgh3[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,4) == "Wgh3" && var != ""  )
                           { print " "substr($1,1,4)" = "var coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${microphys[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,9) == "microphys" && var != ""  )
                           { print " "substr($1,1,9)" = "var coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${slhum[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,5) == "slhum" && var != ""  )
                           { print " "substr($1,1,5)" = "var coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${forcings_weight_d[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,17) == "forcings_weight_d" && var != ""  )
                           { print " "substr($1,1,17)" = "var coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${forcings_weight_t[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,17) == "forcings_weight_t" && var != ""  )
                           { print " "substr($1,1,17)" = "var coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${forcings_weight_m[x]}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,17) == "forcings_weight_m" && var != ""  )
                           { print " "substr($1,1,17)" = "var coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cp ${path}/parmodel_test ${path}/PARMODEL
echo "cp "${path}/parmodel_test" "${path}/PARMODEL

#erg##########################################################

# Save run details
cp ${path}/PARMODEL ${dirfNameOutput}
echo "cp "${path}/PARMODEL" "${dirfNameOutput}

# copy namelist to executable area
#erg cp ${path}/PARMODEL ${SUBMIT_HOME}/agcm1d_cptec_inpe/PHYSCS-2.0.0/model/exec/
#erg cp ${path2}/model/exec/ParModel_MPI ${SUBMIT_HOME}/agcm1d_cptec_inpe/PHYSCS-2.0.0/model/exec/
cp ${path}/PARMODEL ${path2}/model/exec/
echo "cp "${path}/PARMODEL" "${path2}/model/exec/
#erg cp ${path}/SOND_IN ${path2}/model/datain/
#erg cp ${path}/FORCINGS_ASCII ${path2}/model/datain/
###erg cp ${path2}/model/exec/ParModel_MPI ${DataIn}/../exec/
#
#
######run
######run

pwd > ${path2}/run/model.in
echo "${DataIn}" >> ${path2}/run/model.in  #erg  "${SUBMIT_HOME}/PHYSCS-2.0.0/model/datain" >> ${path2}/run/model.in
echo "${DataOut}/${Exp[x]}"   >> ${path2}/run/model.in   #erg "${WORK_HOME}/PHYSCS-2.0.0/model/dataout/Exp${Exp[x]}"   >> ${path2}/run/model.in

ulimit -s unlimited
cat <<EOT1 > ${path2}/run/xmit_${Exp[x]}.sh
#!/bin/bash
#
ulimit -s unlimited
#erg cd ${SUBMIT_HOME}/PHYSCS-2.0.0/model/exec
cd ${path2}/model/exec
#erg ${SUBMIT_HOME}/PHYSCS-2.0.0/model/exec/ParModel_MPI < ${path2}/run/model.in
#export GFORTRAN_CONVERT_UNIT=swap
${path2}/model/exec/ParModel_MPI.exe < ${path2}/run/model.in
EOT1


chmod 777 ${path2}/run/xmit_${Exp[x]}.sh
${path2}/run/xmit_${Exp[x]}.sh


#cp ${path}/PARMODEL.BKP.ENVER ${path}/PARMODEL
#Cleaning xmit
rm ${path2}/run/xmit_${Exp[x]}.sh
x=`expr $x + 1`


#!Jhonatan 
#python and cdo  programs #Location $fpython
sed   -e "s;##Experimentlabelbam##;${Exp};g" \
      -e "s;##labelofpythonfiles##;${Exp};g" \
      -e "s;##DataOut##;${DataOut}${Exp}/;g" \
      -e "s;##LocationPythonFiles##;${fpython};g" \
      -e "s;##lev##;${LV};g" \
      ${fpython}runpython.sh > ${DataOut}${Exp}/runpython${Exp}.sh 


cd ${DataOut}${Exp}

chmod 777  runpython${Exp}.sh 
bash runpython${Exp}.sh 

done

