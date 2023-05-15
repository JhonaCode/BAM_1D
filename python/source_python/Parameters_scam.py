
########################################
# Function to load the libraries   
# and load the files to be read  
########################################
# Jhonatan A. A. Manco
# Oct 18/2022
########################################


import  numpy               as  np

import  matplotlib          as mpl

import  matplotlib.pyplot   as plt

import  numpy.ma            as ma

#to work with date in plots 
import  matplotlib.dates as mdates

# python library to work with netcdf4 
from    netCDF4         import Dataset

# to save the time coordinate in specific format 
from    netCDF4         import num2date, date2num

###To the local and not local language in the data
import  locale

######################################################
#My files
######################################################
from files_direction import *


#import    iop observed data 
from    Parameters_files.Parameters_forcing_iop_old  import * 


#To load the variables of the scam experiment
import  var_files.var_scam_goa_iop1        as  v_iop1

#To load the variables of the scam experiment
import  var_files.var_scam_goa_iop2        as  v_iop2

import  var_files.var_scam  as  v_scam


##Function to trandfform data in indices 
import  source.data_own as down

# To change the plot parameter 
import  source.plotparameters        as	plotpar

import  source.figure_own            as fown

# function plot
#import function_plot as fp
# to work without display
#plt.switch_backend('agg')


def color_exp(hour):

    line=[1,0]
    color='k'

    if  hour==0:
    
        line=[3,2,1,2]
        color='black'
    
    if  hour==1:
    
        #line=[2,2,1,2]
        color='cyan'
    
    
    if   hour==2:
    
        line=[2, 1]
        color='b'
    
    elif  hour==3:
    
        #line=[3, 1]
        color='g'
    
    elif  hour==4:
    
        line=[4, 1]
        color='r'
    
    elif  hour==5:
    
        #line=[1,1]
        color='tab:orange'
    
    elif  hour==6:
    
        line=[1,2,1,2]
        color='m'
    
    elif  hour==7:
    
        #line=[2,1,1,3]
        color='tab:brown'
    
    elif  hour==8:
    
        line=[2,1,5,3]
        color='tab:purple'
    
    elif  hour==9:
    
        #line=[4,2,1,2]
        color='y'
    
    elif  hour==10:
    
        line=[1,2,4,2]
        color='c'
    
    return line,color

computer='/home/jhona'

file_1        = '%s/repositories/scam_docker/scam_docker/shallow_tutorial/cases/shallow.FSCAM.goa_iop1_scm/run/shallow.FSCAM.goa_iop1_scm.cam.h0.2014-02-15-00000.nc'%(computer) 
calendar=["days  since 2014-02-15 00:00:00 +04:00:00",'gregorian']
iop1 = v_scam.ncload(file_1,calendar)
#
file_2        = '%s/repositories/scam_docker/scam_docker/shallow_tutorial/cases/shallow_prescribed.FSCAM.goa_iop1_scm/run/shallow_prescribed.FSCAM.goa_iop1_scm.cam.h0.2014-02-15-00000.nc'%(computer) 
calendar=["days  since 2014-02-15 00:00:00 +04:00:00",'gregorian']
iop1_pre = v_scam.ncload(file_2,calendar)

#
file_3        = '%s/repositories/scam_docker/scam_docker/shallow_tutorial/cases/shallow.FSCAM.goa_iop2_scm/run/shallow.FSCAM.goa_iop2_scm.cam.h0.2014-09-01-00000.nc'%(computer) 
calendar=["days  since 2014-09-01 00:00:00 +04:00:00",'gregorian']
iop2_scm = v_scam.ncload(file_3,calendar)

#
file_4        = '%s/repositories/scam_docker/scam_docker/shallow_tutorial/cases/shallow_prescribed.FSCAM.goa_iop2_scm/run/shallow_prescribed.FSCAM.goa_iop2_scm.cam.h0.2014-09-01-00000.nc'%(computer) 
calendar=["days  since 2014-09-01 00:00:00 +04:00:00",'gregorian']
iop2_pre_scm = v_scam.ncload(file_4,calendar)


file_5        = '%s/repositories/scam_docker/scam_docker/shallow_tutorial/cases/shallow_prescribed.FSCAM.goa_iop2/run/shallow_prescribed.FSCAM.goa_iop2.cam.h0.2014-09-01-00000.nc'%(computer) 
calendar=["days  since 2014-09-01 00:00:00 +04:00:00",'gregorian'] 
iop2_pre = v_scam.ncload(file_5,calendar)

file_5        = '%s/repositories/scam_docker/scam_docker/shallow_tutorial/cases/shallow.FSCAM.goa_iop2/run/shallow.FSCAM.goa_iop2.cam.h0.2014-09-01-00000.nc'%(computer) 
calendar=["days  since 2014-09-01 00:00:00 +04:00:00",'gregorian']
iop2 = v_scam.ncload(file_5,calendar)

file_6        = '%s/repositories/scam_docker/scam_docker/shallow_tutorial/cases/uw.FSCAM.goa_iop2_scm_UW/run/uw.FSCAM.goa_iop2_scm_UW.cam.h0.2014-09-01-00000.nc'%(computer) 
calendar=["days  since 2014-01-01 00:00:00 +04:00:00",'gregorian']
iop2_uw = v_scam.ncload(file_6,calendar)

file_8        = '%s/repositories/scam_docker/scam_docker/shallow_tutorial/cases/sh_ca_uw.FSCAM.ShCa_scam_scm/run/sh_ca_uw.FSCAM.ShCa_scam_scm.cam.h0.2014-01-01-00000.nc'%(computer) 
calendar=["days  since 2014-01-01 00:00:00 +04:00:00",'gregorian']
shca_uw = v_scam.ncload(file_8,calendar)


file_7        = '%s/repositories/scam_docker/scam_docker/shallow_tutorial/cases/sh_ca_uw_cam5.FSCAM.ShCa_scam_scm/run/sh_ca_uw_cam5.FSCAM.ShCa_scam_scm.cam.h0.2014-01-01-00000.nc'%(computer)
calendar=["days  since 2014-01-01 00:00:00 +04:00:00",'gregorian']
shca_c5 = v_scam.ncload(file_7,calendar)

file_9        = '%s/repositories/scam_docker/scam_docker/shallow_tutorial/cases/sh.FSCAM.bomex/run/sh.FSCAM.bomex.cam.h0.1969-06-25-00000.nc'%(computer)
calendar=["days  since 1969-06-25 00:00:00 +00:00:00",'gregorian']
shbomex = v_scam.ncload(file_9,calendar)
