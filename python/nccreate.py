#################################3#
# Program to create  a meteorological  data in a .nc file 
# Parameters: Parametersnccreate.py
# Specific the variables to save and the initial and final time. 
# Obs:Only work with bam1d, no Long and Lat
# Create by: Jhonatan Aguirre 
# Date:11/01/2020
# working: no ###################################
# 

#To load the parameter that 
#will be plotted 

from  #Parametersnccreated#  import * 

#Mathematic library 
import  numpy       as     np

#import  matplotlib  as     mpl
import  matplotlib as mpl

#import  matplotlib  as     pl
import matplotlib.pyplot as plt


#To work with date in plots 
import matplotlib.dates as mdates

# Python library to work with Netcdf4 
from    netCDF4         import Dataset

# To save the time coordinate in specific format 
from    netCDF4         import num2date, date2num

#divergin color maps
#from    diverging_map    import * 

# Python module to read the information of the date
from    Ncdump     import * 

# Python standard library datetime  module
import datetime as dt  

import time 

#conda install basemap
# To plot the map 
from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid

# To change the plot parameter 
from   	plotparameters 		import 	*

#to work with list of files
#import tkFileDialog
import tkinter.filedialog

#Pressure nivel 
Z=[1.000000, 0.989934, 0.974009, 0.954290, 0.930081, 0.900698, 0.865537, 0.824114, 0.776260, 0.722185, \
   0.662603, 0.598714, 0.532217, 0.465086, 0.399394, 0.337014, 0.279476, 0.227787, 0.182459, 0.143533, \
   0.110697, 0.083428, 0.061061, 0.042912, 0.028306, 0.016629, 0.007338, 0.003669]


start = dt.datetime.strptime(dayi,'%Y%m%d%H')

end   = dt.datetime.strptime(dayf,'%Y%m%d%H') #+ dt.timedelta(hours=26)

delta=(end-start)
#print delta

def hour_range(start, end):
    while start < end:
        yield start
        start += dt.timedelta(hours=step_hours)

#For the string list 
#date = [h.strftime('%Y%m%d%H') for h in hour_range(start, end)]
#For the datetime list 
date     = [h for h in hour_range(start, end)]

date_strg= [day.strftime('%Y%m%d%H') for day in date]


#datestr= date[].strftime('%Y%m%d%H')  


#date = [h.strftime('%Y%m%d%H') for h in hour_range(start, end)]

#Number of days to plot 
ndtp=len(date) 



#Creating a list
file_date=[]
#
nc_fid=[]

#Date=list()

for i in range(0,ndtp):

    #File to load
    file_date.append("GFCTNMC%s%sF.fct.T062L28.nc"%(di,date_strg[i]))

    # Your files location
    nc_f = '%s%s'%(file_l,file_date[i])  

    # Dataset is the class behavior to open the file
    # and create an instance of the ncCDF4 class
    nc_fid.append(Dataset(nc_f, 'r'))    

    #nc_attrs, nc_dims, nc_vars = ncdump(nc_fid[i])


# Open a new NetCDF file to write the data to. For format, you can choose from
# 'NETCDF3_CLASSIC', 'NETCDF3_64BIT', 'NETCDF4_CLASSIC', and 'NETCDF4'

nc_file1 = Dataset('%s.nc'%(file_outnc), 'w', format='NETCDF4')
#w_nc_fid = Dataset('outt.nc', 'w', format='NETCDF_3G4BIT')

nc_file1.description  ='Data INPE/CPTEC/BAM 1_D from %s to %s.'%(date[0],date[ndtp-1])

nc_file1.history      ="Created %s "%(time.localtime())

nc_file1.history      ="Created by Jhonatan Aguirre Manco  " + time.ctime(time.time())


nc_file1.source       ="Bam_1d"


#Group to concatenate the variables 
nc_grp = nc_file1.createGroup('Bam1D_group_variables')


#A Python string is used to set the name of the dimension,
#and an integer value is used to set the size.
#To create an unlimited dimension 
#(a dimension that can be appended to), the size value is set to None or 0.

#Dimesion important to create the groups 
time    =nc_file1.createDimension('time', None)
level   =nc_file1.createDimension('level', None)

#To create a netCDF variable, use the createVariable method of a 
#Dataset or Group instance.
#The createVariable method has two mandatory arguments, 
#the variable name (a Python string), and the variable datatype
#The variable's dimensions are given by a tuple containing the dimension names
#defined previously with createDimension


time= nc_file1.createVariable('time',nc_fid[0].variables['time'].dtype,('time',))
#tkenall1= nc_file1.createVariable('tkenall1',nc_fid[0].variables['tken'].dtype,('time','level',))

time.units        = "hours since %s-%s-%s %s"%(dayi[0:4],dayi[4:6],dayi[6:8],dayi[8:10])
time.calendar     = "gregorian"


#Lists of ncvaribles to write in the file  
variablenc=[]
#Lists to save the varaible in all time  
variableaux=[]

#One variable add
#var12  =  nc_fid[0].variables['prec'][:]
#print var12.shape
#var22  =  nc_fid[0].variables['tken'][:]
#print var22.shape

#Time of the dates.
time[:]    = date2num(date[:],units=time.units,calendar=time.calendar)


for i in range(1,nvtp+1):

    #To chante the variable name with i 
    key1 = 'var{}'.format(i)

    #To kwnow the kind of variable, levels or not levels 
    var  =  nc_fid[0].variables["%s"%(locals()[key1][:])]
    shapev= var.shape[1]

    #Levels variables
    if shapev>1:

        variablenc.append(nc_file1.createVariable('%s'%(locals()[key1]),'f8',('time','level',)))

        for j in range(0,ndtp):

            var  =  nc_fid[j].variables["%s"%(locals()[key1][:])]

            variablenc[i-1][j,:] = var[:] 

    #No Levels variables
    else:
        variablenc.append(nc_file1.createVariable('%s'%(locals()[key1]),'f8',('time',)))

        for j in range(0,ndtp):

            var  =  nc_fid[j].variables["%s"%(locals()[key1][:])]

            variablenc[i-1][j] = var[:] 

    #Allocate variables units
    key2 = 'var{}units'.format(i)
    variablenc[i-1].units = "%s"%(locals()[key2])

#
print(variablenc)

## close the new file
nc_file1.close()  


#plt.show()

		

