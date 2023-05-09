#"""
######################################
#Program to plot meteorological date 
#using python with NetCdf
#eurf Temp 
#Surf Temp  Create by: Jhonatan Aguirre 
#Surf Temp  Date:28/12/2021
#
#working: 
#
######################################
#"""
# To activate this environment, use
#
#     $ conda activate py37
# Went panda is use
# To deactivate an active environment, use
#
#     $ conda deactivate

################
###My functions
################

#path of the ncfile
from    source_python.Parameters##label##  import file_l, file_o, di

#To load the variables, in this file are the variavbles to read of 
#nc file. variabletoload.py
from    source_python.variabletoload##varload##     import * 

# To change the plot parameter 
import 	source_python.plotparameters 		as pp

#To plot the diurnal cycle
import  source_python.diurnal                  as dc



################
##Python functions
################

import numpy        as np

import matplotlib   as mpl

import matplotlib.pyplot as plt

#To work with date in plots 
import matplotlib.dates  as mdates

# Python standard library datetime  module
import datetime as dt  


#Dictionay to defined the experiment to run 

exp= {'name':'iop1','exp_name':'IOP1','data':ncload(file_l)}

#Data to plot of the experiment 
ex = exp['data']


#Diurnal cycle calculation 
meanprec,hour  = dc.diurnal_function(ex.data,ex.prec)

meanlhflx,hour = dc.diurnal_function(ex.data,ex.clsf)

meanshflx,hour = dc.diurnal_function(ex.data,ex.cssf)


#################################################
#used user parameter to plot(source/plotparameter.py)
mpl.rcParams.update(pp.params)


#Temporal figures.
#################################################

fig = plt.figure()
ax  = plt.axes()

fig,ax=pp.axis_format(fig,ax)

plt.plot(ex.data, ex.prec[:],'k-',marker='',label=exp['exp_name'] )

#Axis label
plt.ylabel(r'Precipitation $\mathrm{ [mm/h]}$') 

plt.legend(frameon=False)

#plt.axis([-0.4, 23.4, 0.1, 0.80])

plt.savefig('%s/prec_%s.pdf'%(file_o,exp['name']), format='pdf', dpi=1000)


##################################################3
#Without diurnal cycle
#Precipitation
fig = plt.figure()
###New axis
ax  = plt.axes()

fig,ax=pp.axis_format(fig,ax)

plt.plot(ex.data, ex.clsf,'m-',marker='',label=exp['exp_name'] )

#plt.axis([-0.4, 23.4, 0.1, 0.80])

plt.savefig('%s/lsf_%s.pdf'%(file_o,exp['name']), format='pdf', dpi=1000)


#Sensible
##################################################3
#Without diurnal cycle
#Precipitation
fig = plt.figure()

###New axis
ax  = plt.axes()

fig,ax=pp.axis_format(fig,ax)

plt.plot(ex.data, ex.cssf,'ko-',marker='',label=exp['exp_name'] )

plt.savefig('%s/ssf_%s.pdf'%(file_o,exp['name']), format='pdf', dpi=1000)


#Diurnal Cycle 
###################################################################
#Precipitation 

fig = plt.figure()
###New axis
ax  = plt.axes()

######################
plt.plot(hour,meanprec,'ko-',label=exp['exp_name']) 

plt.savefig('%s/mean_prec_%s.pdf'%(file_o,exp['name']), format='pdf', dpi=1000)

######################

fig = plt.figure()
###New axis
ax  = plt.axes()


plt.plot(hour      ,meanshflx   ,'k-',marker='o',label=exp['exp_name'] ) 

#plt.plot(hour_exp,meanshflx_exp   ,'c-',marker='P',label="Surface Sensible heat Flux  GOA") 
plt.xlabel(r' Hour')
plt.ylabel(r'Sensible Heat Flux $\mathrm{[WM^{-2}]}$') 

plt.savefig('%s/mean_ssf_%s.pdf'%(file_o,exp['name']), format='pdf', dpi=1000)

###################################################################
#latent Heat flux 

fig = plt.figure()
###New axis
ax  = plt.axes()
#scale
######################
plt.plot(hour      ,meanlhflx      ,'k-',marker='o',label=exp['exp_name']) 

#plt.plot(hour_exp  ,meanlhflx_exp ,'c-',marker='P',label=" Surface Latent heat Flux GOA") 

plt.axis([-0.4, 23.4, -650, 600.00])
##With legends 
plt.legend()
ax.legend(frameon=False)

#Axis label
#plt.xlabel(r' Hour')
plt.ylabel(r'Latent Heat Flux $\mathrm{[WM^{-2}]}$') 

plt.savefig('%s/mean_lsf_%s.pdf'%(file_o,exp['name']), format='pdf', dpi=1000)

###################################################################

plt.show() 




