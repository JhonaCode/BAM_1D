#!/bin/bash 
# Script to create NetCDF files from BAM_1D binary files
# -------------------------------- WARNING ------------------------------
#
# Not method was found to change endianness of the input binary before write the NetCDF file. 
# input binary is in Big_Endian byte ordering
#
# Levels should be modified for each experiment
#
# -------------------------------- WARNING ------------------------------
# Enver Ramirez 
# April 12, 2019 
# December 19, 2019

#Modify
#Jhonatan Aguirre Manco.
# January  20, 2020 
#idx funcionando


#Diretorio dos arquivos 
fdir=#dirctl#
#Diretorio de saida dos arquivos 
fdirout=#dirnc#

vertRes=#lev#

##t initial date
#s="00z01Oct2011"
### end date
#e="00z10Oct2011"

s="00z15Feb2014"
## end date
e="00z10May2014"


strip=(Y m d H)
idx=0
for x in "${strip[@]}"
do
   t0[idx]=$(date -u -d "${s} +0 days" "+%${x}")
   tf[idx]=$(date -u -d "${e} +0 days" "+%${x}")
   idx=`expr $idx + 1`
done

LABELI="${t0[3]}-${t0[2]}-${t0[1]},${t0[0]}"
LABELF="${tf[3]},${tf[2]},${tf[1]},${tf[0]}"


#Criar um novo arquivo 
cat > newzaxis << eof
zaxistype = pressure
size      = ${vertRes}
name      = lev
longname  = pressure
units     = mb
levels    = 998.784000 
            988.730240 
            972.824605 
            953.129583 
            928.950021 
            899.602751 
            864.484507 
            823.111877 
            775.316067 
            721.306823 
            661.797274 
            597.985963 
            531.569824 
            464.520455 
            398.908336 
            336.604190 
            279.136157 
            227.510011 
            182.237129 
            143.358463 
            110.562392 
            83.326551 
            60.986749 
            42.859819 
            28.271579 
            16.608779 
            7.329076 
            3.664538 
eof


ls ${fdir}*${t0[0]}*${t0[0]}*F.fct.*L${vertRes}.ctl > lista


echo ${fdir} 


#cdo settaxis,<startdate>,<starttime>,<increment> -setcalendar,360_day -importbinary  ifile.ctl  ofile.nc

if [ ! -d ${fdir}ncfiles ]; then
        mkdir -p ${fdir}ncfiles  
fi

#To put the date time in the file.
#Depends on the initial date

idx=00

for x in `cat lista`
        do
        #basename — Retorna apenas a parte que corresponde ao nome do arquivo de um caminho/path
        #newfile=`basename $x `
        #tirando o .ctl
        newfile=`basename $x ctl`
        echo $newfile
        
        #substituir, igual ao vim %s
        #comando do grads nos ctls
        sed -i 's/OPTIONS SEQUENTIAL YREV/OPTIONS SEQUENTIAL YREV BIG_ENDIAN/g' ${x}
        
        LABELI="${t0[0]}-${t0[1]}-${t0[2]}t${t0[3]}:00:00"
        LABELF="${tf[0]}-${tf[1]}-${tf[2]}t${tf[3]}:00:00"
        
        cdo -f nc import_binary ${x} temp.nc
        cdo  -r settaxis,${LABELI},${idx}:00:00,1hour temp.nc ${fdirout}ncfiles/${newfile}nc 
        
        
        idx=`expr $idx + 1`
        
done

rm temp.nc

#Juntar todos os .nc em um unico binario. 
#maximo 256
cdo mergetime *.nc bam1d.nc

rm GFCTNMC*.nc

#Juntar todos os .nc em um unico binario se todos estiver em ordem 
#cat *.ct bam1d.nc




