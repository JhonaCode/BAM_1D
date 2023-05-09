#!/bin/bash
#help#
#****************************************************************************#
# Script to run agcm 1D, version 4.0.0 model on CRAY.
#
# usage: runbeta_after_double_1_sigma CaseName
# CaseName: Is the name of the experiment. The experiment name is linked
#           to a directory containing initial condition, sonding profile 
#           (SOND_IN) and boundary condition (FORCINGS_ASCII or FORCING_IN).
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
#help#
export HOME1=`pwd`

DataIn=${HOME1}/../model/datain/
DataOut=${HOME1}/../model/dataout/



#python options 
#Jhonatan
fpython=${HOME1}/../python/


echo $DataIn

Exp=(_2AMZ)     ### Exp_x  x=1,2,3....

# Checking arguments
if [ "${1}" = "help" -o -z "${1}" ]
then
  cat < ${0} | sed -n '/^#help#/,/^#help#/p'
  echo "Available data directories are in: "
  echo "       "$DataIn
  exit 1
fi


# numero de niveis verticais
if [ -z ${LV} ];then
   #LV=28
   LV=42
fi

path=`pwd`                                                             #### get direc path=.../run/
path2=`echo ${path} | awk '{print substr($1,1,index($1,"/run")-1)}'`   #### path2=.../BAM_1D/
CaseName=${1}


if [ ! -d "${DataIn}/${CaseName}" ]
then
 echo "Experiment "${CaseName}" does not exist"
 echo "Available experiments are in:"
 echo ${DataIn}
 exit 1
fi

x=0
upx=${#Exp[@]}
while [ "$x" -lt "$upx" ]
do

#Check existence of output dir
dirfNameOutput=${DataOut}Exp${Exp[x]}/
path_in=${DataIn}
if [ -d "$dirfNameOutput" ]
then
    echo "directory $dirfNameOutput exist"
## rm pre-existing file
rm  ${dirfNameOutput}/*
else
    mkdir $dirfNameOutput   ###### make directorio  /BAM_1D//model/dataou_1
fi

# copy CaseName data to datain (IC, BC, PARMODEL default)
if [ "$x" -eq "0" ]
then 
  echo "copy IC, BC, PARMODEL from "${CaseName}
  echo "cp "${DataIn}/${CaseName}/*" "${DataIn}/
  echo "cp "${DataIn}/${CaseName}/PARMODEL" "${path}/     
  cp ${DataIn}/${CaseName}/* ${DataIn}/                    #### copy IC, BC, Forcing  to BAM_1D/model/datain/ 
  cp ${DataIn}/${CaseName}/PARMODEL ${path}/               #####copy PARMODEL to /run/
else
  echo "jumping copy" 
fi
##----------------------Temporary PARMODEL to define a new directory for output

cp ${path}/PARMODEL ${path}/parmodel_test
echo "cp "${path}/PARMODEL ${path}/parmodel_test
echo ${Exp[x]}
aspa="'"
coma=","

cat ${path}/parmodel_test  | awk -v var="${dirfNameOutput}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,14) == "dirfNameOutput" && var != ""  )
                           { print " "substr($1,1,14)" = "aspa var aspa coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cat ${path}/parmodel_test  | awk -v var="${path_in}" -v aspa=$aspa -v coma=$coma '{if (substr($1,1,7) == "path_in" && var != ""  )
                           { print " "substr($1,1,7)" = "aspa var aspa coma }
                          else 
                           { print $0 }
                          }' > ${path}/parmodel_test_$x; cp ${path}/parmodel_test_$x ${path}/parmodel_test

cp ${path}/parmodel_test ${path}/PARMODEL
echo "cp "${path}/parmodel_test" "${path}/PARMODEL

#erg##########################################################

# Save run details
cp ${path}/PARMODEL ${dirfNameOutput}                   ####copy to  /dataout_1/
echo "cp "${path}/PARMODEL" "${dirfNameOutput}          

# copy namelist to executable area
cp ${path}/PARMODEL ${path2}/model/exec/                #### copy PARMODEL to .../BAM_1D/model/exec/
echo "cp "${path}/PARMODEL" "${path2}/model/exec/

##########################################################
###RUN
pwd > ${path2}/run/model.in                     ####  get .../BAM_1D/run/model.in   
echo "${DataIn}" >> ${path2}/run/model.in 
echo "${DataOut}/Exp${Exp[x]}"   >> ${path2}/run/model.in

ulimit -s unlimited
cat <<EOT1 > ${path2}/run/xmit_Exp${Exp[x]}.sh       ####  make script to exe...../BAM_1D/run/xmit_exp_1.sh 
#!/bin/bash
#
ulimit -s unlimited
cd ${path2}/model/exec
${path2}/model/exec/ParModel_MPI.exe < ${path2}/run/model.in
EOT1

chmod 777 ${path2}/run/xmit_Exp${Exp[x]}.sh
${path2}/run/xmit_Exp${Exp[x]}.sh

#Cleaning xmit
rm ${path2}/run/xmit_Exp${Exp[x]}.sh parmodel_test_$x 
rm ${path2}/run/parmodel_test  PARMODEL model.in 
rm ${path2}/model/datain/* 
x=`expr $x + 1`


mkdir ${DataOut}Exp${Exp}/figures_out


echo ${DataOut}Exp${Exp}

#!Jhonatan 
#python and cdo  programs #Location $fpython
sed   -e "s;##Experimentlabelbam##;${Exp};g" \
      -e "s;##labelofpythonfiles##;${Exp};g" \
      -e "s;##DataOut##;${DataOut}Exp${Exp}/;g" \
      -e "s;##LocationPythonFiles##;${fpython};g" \
      -e "s;##lev##;${LV};g" \
      ${fpython}runpython.sh > ${DataOut}Exp${Exp}/runpython${Exp}.sh 


cd ${DataOut}Exp${Exp}

chmod 777  runpython${Exp}.sh 
bash runpython${Exp}.sh 



done
