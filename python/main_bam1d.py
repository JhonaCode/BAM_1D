#################################3# # Program to plot meteorological date 
# using python with NetCdf
#eurf Temp 
#Surf Temp  Create by: Jhonatan Aguirre 
#Surf Temp  Date:28/12/2021
# working: no ###################################

# To activate this environment, use
#
#     $ conda activate py37
# Went panda is use
# To deactivate an active environment, use
#
#     $ conda deactivate


#path of the ncfile
from   Parameters_##label## import * 

#To load the variables, in this file are the variavbles to read of 
#nc file. variabletoload.py
from    variabletoload##varload##    import *

import numpy       as     np

import  matplotlib as mpl

import matplotlib.pyplot as plt

import numpy.ma as ma

#To work with date in plots 
import matplotlib.dates as mdates

# Python library to work with Netcdf4 
from    netCDF4         import Dataset

# To save the time coordinate in specific format 
from    netCDF4         import num2date, date2num


###To the local and not local language in the data 
import locale


#divergin color maps
#from    diverging_map    import * 

# Python standard library datetime  module
import datetime as dt  

# To plot the map 
#from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid

# To change the plot parameter 
from   	plotparameters 		import 	*

#To plot the diurnal cycle
from    diurnal    import *

#to work with list of files
#import tkFileDialog 

import cftime as cf
#to plot cftime
#pip install nc-time-axis

import nc_time_axis


#Pressure nivel 
Z=[1.000000, 0.989934, 0.974009, 0.954290, 0.930081, 0.900698, 0.865537, 0.824114, 0.776260, 0.722185, \
   0.662603, 0.598714, 0.532217, 0.465086, 0.399394, 0.337014, 0.279476, 0.227787, 0.182459, 0.143533, \
   0.110697, 0.083428, 0.061061, 0.042912, 0.028306, 0.016629, 0.007338, 0.003669]


#load variables file

##label##=ncload(file_l)


def axis_format():
    #TO put in english see Parameter to more information
    locale.setlocale(locale.LC_ALL, 'en_IN')

    #minor axis
    formatter = nc_time_axis.CFTimeFormatter("%d", "noleap")
    locator=nc_time_axis.NetCDFTimeDateLocator(15,"noleap")
    ax.xaxis.set_minor_formatter(formatter)
    ax.xaxis.set_minor_locator(locator)

    # Set major
    locator=nc_time_axis.NetCDFTimeDateLocator(1,"noleap")
    formatter = nc_time_axis.CFTimeFormatter("\n%b", "noleap")
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    plt.legend(frameon=False)

    return



# Experimental data 
#nc_data_f = '~/repositories/bam_1d/model/datain/GOA_IOP1/forcing_goamazon_IOP1.nc'  
#nc_data_f = './forcing_goamazon_IOP1.nc'  

#nc_data = Dataset(nc_data_f, 'r')    
#nc_attrs2, nc_dims2, nc_vars2 = ncdump(nc_data)

####WARNING: time does not contain variable attributes
####TIME
###tsec_exp  = nc_data.variables['tsec'][:]
###
###t_units =  nc_data.variables['tsec'].units
###
###t_cal =  nc_fid.variables['time'].calendar
###
###tsecd   = num2date(tsec_exp[:],units=t_units)#,calendar=t_cal)

#Calculations 

#Saldo de onda curta: NetOC = OCIS-OCES
netoc   = iop1.ocis-iop1.oces

#Saldo de onda longa: NetOL = OLIS-OLES
#netol   = olis-oles

#Warning
#Segundo o clirad aqui e +
netol   = iop1.olis+iop1.oles
#mas os dois valores saem positivos
netol   = iop1.olis-iop1.oles

#Saldo de onda curta + longa: NetOCOL = NetOC + NetOL
netocol = netoc+netol 


meanprec,hour  = diurnal_function(iop1.data,iop1.prec)

meanlhflx,hour = diurnal_function(iop1.data,iop1.clsf)

meanshflx,hour = diurnal_function(iop1.data,iop1.cssf)

print(meanshflx)
print(hour) 


#####EXPERIMENT
####
#####Precipitation 
####meanprec_exp,hour_exp = diurnal_function_exp(tsecd,prec_exp)
####
#####Net onda curta onda longa 
####meannet_exp,hour_exp  = diurnal_function_exp(tsecd,netocol_exp)
####
####
#####Surfface temperature 
####meantg_exp,hour_exp    = diurnal_function_exp(tsecd,tg_exp)
####meantsair_exp,hour_exp = diurnal_function_exp(tsecd,tsair_exp)
####
#####heat  
####meanlhflx_exp,hour_exp = diurnal_function_exp(tsecd,lhflx_exp)
####meanshflx_exp,hour_exp = diurnal_function_exp(tsecd,shflx_exp)
####
#####flux  
####meanocis_exp,hour_exp = diurnal_function_exp(tsecd,ocis_exp)
####meanoces_exp,hour_exp = diurnal_function_exp(tsecd,oces_exp)
####meanolis_exp,hour_exp = diurnal_function_exp(tsecd,olis_exp)
####meanoles_exp,hour_exp = diurnal_function_exp(tsecd,oles_exp)


#used user parameter to plot(plotparameter.py
mpl.rcParams.update(params)

#Latent
##################################################3
#Without diurnal cycle
#Precipitation
fig = plt.figure()

###New axis
ax  = plt.axes()

axis_format()

plt.plot(iop1.data, iop1.prec,'m-',marker='',label='IOP1' )

#Axis label
plt.ylabel(r'Precipitation $\mathrm{ [mm/h]}$') 

#plt.axis([-0.4, 23.4, 0.1, 0.80])

#plt.savefig('%sprec_GOA.pdf'%(file_fig), format='pdf', dpi=1000)

#Latent
##################################################3
#Without diurnal cycle
#Precipitation
fig = plt.figure()
###New axis
ax  = plt.axes()

axis_format()

plt.plot(iop1.data, iop1.clsf,'m-',marker='',label='IOP1' )

#plt.axis([-0.4, 23.4, 0.1, 0.80])

#plt.savefig('%sprec_GOA.pdf'%(file_fig), format='pdf', dpi=1000)

#Sensible
##################################################3
#Without diurnal cycle
#Precipitation
fig = plt.figure()
###New axis
ax  = plt.axes()

axis_format()

plt.plot(iop1.data, iop1.cssf,'m-',marker='',label='IOP1' )

#plt.savefig('%sprec_GOA.pdf'%(file_fig), format='pdf', dpi=1000)

#Diurnal Cycle 
###################################################################
#Precipitation 

fig = plt.figure()
###New axis
ax  = plt.axes()

######################
plt.plot(hour,meanprec,'ko-',label="IOP1") 

#plt.plot(hour_exp,meanprec_exp,'c-',marker= 'P',label="Precipitation_GOA") 

######################

fig = plt.figure()
###New axis
ax  = plt.axes()


plt.plot(hour      ,meanshflx   ,'k-',marker='o',label="Bam_1d Tarasova"              ) 

#plt.plot(hour_exp,meanshflx_exp   ,'c-',marker='P',label="Surface Sensible heat Flux  GOA") 
plt.xlabel(r' Hour')
plt.ylabel(r'Sensible Heat Flux $\mathrm{[WM^{-2}]}$') 

#plt.savefig('%ssensible_GOA.pdf'%(file_fig), format='pdf', dpi=1000)

###################################################################
#latent Heat flux 

fig = plt.figure()
###New axis
ax  = plt.axes()
#scale
######################
plt.plot(hour      ,meanlhflx      ,'k-',marker='o',label=" Bam_1d Tarasova") 

#plt.plot(hour_exp  ,meanlhflx_exp ,'c-',marker='P',label=" Surface Latent heat Flux GOA") 

plt.axis([-0.4, 23.4, -650, 600.00])
##With legends 
plt.legend()
ax.legend(frameon=False)
#Axis label
#plt.xlabel(r' Hour')
plt.ylabel(r'Latent Heat Flux $\mathrm{[WM^{-2}]}$') 

#plt.savefig('%slatent_GOA.pdf'%(file_fig), format='pdf', dpi=1000)

###################################################################

plt.show() 




