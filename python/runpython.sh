#!/bin/bash
#################################3#
# Program  read the .ctl files, which are the 
# out of the Bam-1d program, transform its 
# in .nc files in a new file 'ncfile' in 
# the ctl adress. 
#
#This transformation is make with cdo.
# Create2NetCDF.sh
#
# This program also create the a specific 
# ncfile: outt.nc with specifict dates and 
# variables.  
#
# This creation is make with python .
# python nccreate.py
#
# To modified the varibles to create in outt.nc see:
# Parametersnccreate.py
##################################################
# Create by: Jhonatan Aguirre 
# Date:17/12/2018
# working: no #################################

###############################################
#Inputs
# Exp= Experiment ctl files
# Parametersnccreate.py
# outnc= name of specific file nc

#Name of the Experiment
Exp='##Experimentlabelbam##'

#Specifics the label of the files that 
# will be created. 
Elabel='##labelofpythonfiles##'

#folder exp data location
DataOut=##DataOut##

#where are the python files to cp
fpython=##LocationPythonFiles## 

#####Number of levels
lev=##lev##


#ctl files to transform in nc
fctl=$DataOut #Diretorio de saida dos arquivos 
fnc=$DataOut


echo "this is the path of the nc files $fnc" 

#Name nc specific file 
labeloutnc=bam1d_out_$Elabel
outnc=${fnc}ncfiles/$labeloutnc

###############################################

#Tranform ctl to nc
# if it does not exits.
#Does not like of spaces in defintion 
File="${fctl}ncfiles"


# To check if the ncfiles exits 

##it is necessary the space before and after the corchete
if  [ -d "$File" ]; then

        echo "ncfiles/*.nc exist"
else 
        echo "ncfiles/*.nc not exist, will be created"


        sed  -e "s;#dirctl#;'${fctl}';g" \
             -e "s;#dirnc#;'${fnc}';g" \
             -e "s;#lev#;'${lev}';g" \
             ${fpython}Create2NetCDF.sh > ${DataOut}nccreate_$Elabel.sh 
        
        chmod 777 ${DataOut}nccreate_$Elabel.sh 
        ${DataOut}_nccreate$Elabel.sh
fi


#In Parametersnccreate are the infomation necessary to 
#create the specific nc file, like the variables, the 
#dates and the timestep.


#Copy the funciton necessary to run the python file 

cp ${fpython}Ncdump.py          ${DataOut}
cp ${fpython}diurnal.py         ${DataOut}
cp ${fpython}main_bam1d.py      ${DataOut}
#cp ${fpython}variabletoload  ${DataOut}
cp ${fpython}variabletoload_shallow.py  ${DataOut}
cp ${fpython}plotparameters.py  ${DataOut}

sed -e  "s;#filenc#;${fnc}ncfiles/;g" \
    -e  "s;#fileoutnc#;${outnc};g" \
    ${fpython}Parametersnccreate_shallow.py > ${DataOut}Parameters_$Elabel.py 

sed -e  "s;##label##;$Elabel;g" \
    -e  "s;##varload##;_shallow;g" \
    ${fpython}main_bam1d.py > ${DataOut}main_bam_1d_$Elabel.py 


File2="$outnc.nc"

#it is necessary the space before and after the corchete
if [ -f "$File2" ]; then

        echo "${outnc}.nc  exist"
   
else 
        sed -e "s;#Parametersnccreated#;Parameters_$Elabel;g" \
        ${fpython}nccreate.py > ${DataOut}nc_$Elabel.py 

        echo "${outnc}.nc  not exist,will be created"

        python ${DataOut}nc_$Elabel.py

fi

