################################################# 
# Program to read variable of a nc file 
# using python with NetCdf
# Create by: Jhonatan Aguirre 
# Date:06/02/2020
# working:yes
#################################################

# Python module to read the information of the date
import  numpy as np 

# Python library to work with Netcdf4 
from    netCDF4         import Dataset

# To save the time coordinate in specific format 
from    netCDF4         import num2date, date2num

class variables:

    def __init__(var):

        var.time = 'time' 
        var.data = 'data' 
        var.prec = 'prec' 
        var.temp = 'temp' 
        var.tsfc = 'tsfc' 
        var.clsf = 'clsf' 
        var.cssf = 'cssf' 
        var.scvm = 'scvm' 
        var.pblt = 'pblt' 
        var.pblq = 'pblq' 
        var.lglh = 'lglh' 
        var.lgms = 'lgms' 
        var.vdcc = 'vdcc' 
        var.cvcl = 'cvcl' 
        var.sscl = 'sscl' 
        var.liqm = 'liqm' 
        var.scvh = 'scvh' 
        var.icem = 'icem' 
        var.scld = 'scld' 
        var.pblh = 'pblh' 
        var.cape = 'cape' 
        var.ddmd = 'ddmd' 
        var.cine = 'cine' 
        var.eqpt = 'eqpt' 
        var.ddmu = 'ddmu' 
        var.lev  = 'pre' 
#########################
        var.oces = 'oces' 
        var.ocis = 'ocis' 
        var.olis = 'olis' 
        var.oles = 'oles' 
        var.ocic = 'ocic' 
        var.tsfc = 'tsfc' 
        var.clsf = 'clsf' 
        var.cssf = 'cssf' 
        var.ddde = 'ddde' 
        var.dden = 'dden' 

def ncload(file_l):

    label=variables() 

    # Your filename
    nc_f    = '%s'%(file_l)  

    # Dataset is the class behavior to open the file
    # and create an instance of the ncCDF4 class
    nc_fid = Dataset(nc_f, 'r')    

    #To see the nc file
    #nc_attrs, nc_dims, nc_vars = ncdump(nc_fid)

    label.time    = nc_fid.variables['time'][:]
    
    prec    = nc_fid.variables['prec'][:]  
    #prec to mm/hour
    rho_w   =  997.0 #[kg/m^3]
    #prec    = kg*m-2*day-1*1/rho_w*m^3/kg*1dia/24hour
    #        = 1/(24.0rho_w) [m/hour]*1000mm/1m
    label.prec     = 1000.0/(24.0*rho_w)*prec#[mm/hour]
    
    label.time    = np.squeeze(nc_fid.variables['time'][:])  
    label.prec    = np.squeeze(nc_fid.variables['prec'][:])  
    label.temp    = np.squeeze(nc_fid.variables['temp'][:])  
    label.tsfc    = np.squeeze(nc_fid.variables['tsfc'][:])  
    label.clsf    = np.squeeze(nc_fid.variables['clsf'][:])  
    label.cssf    = np.squeeze(nc_fid.variables['cssf'][:])  
    label.scvm    = np.squeeze(nc_fid.variables['scvm'][:])  
    label.pblt    = np.squeeze(nc_fid.variables['pblt'][:])  
    label.pblq    = np.squeeze(nc_fid.variables['pblq'][:])  
    label.lglh    = np.squeeze(nc_fid.variables['lglh'][:])  
    label.lgms    = np.squeeze(nc_fid.variables['lgms'][:])  
    label.vdcc    = np.squeeze(nc_fid.variables['vdcc'][:])  
    label.cvcl    = np.squeeze(nc_fid.variables['cvcl'][:])  
    label.sscl    = np.squeeze(nc_fid.variables['sscl'][:])  
    label.liqm    = np.squeeze(nc_fid.variables['liqm'][:])  
    label.scvh    = np.squeeze(nc_fid.variables['scvh'][:])  
    label.icem    = np.squeeze(nc_fid.variables['icem'][:])  
    label.scld    = np.squeeze(nc_fid.variables['scld'][:])  
    label.pblh    = np.squeeze(nc_fid.variables['pblh'][:])  
    label.cape    = np.squeeze(nc_fid.variables['cape'][:])  
    label.ddmd    = np.squeeze(nc_fid.variables['ddmd'][:])  
    label.cine    = np.squeeze(nc_fid.variables['cine'][:])  
    label.eqpt    = np.squeeze(nc_fid.variables['eqpt'][:])  
    label.ddmu    = np.squeeze(nc_fid.variables['ddmu'][:])  
    label.oces    = np.squeeze(nc_fid.variables['oces'][:]) 
    label.ocis    = np.squeeze(nc_fid.variables['ocis'][:]) 
    label.olis    = np.squeeze(nc_fid.variables['olis'][:]) 
    label.oles    = np.squeeze(nc_fid.variables['oles'][:])
    label.ocic    = np.squeeze(nc_fid.variables['ocic'][:])
    label.tsfc    = np.squeeze(nc_fid.variables['tsfc'][:])
    label.clsf    = np.squeeze(nc_fid.variables['clsf'][:])
    label.cssf    = np.squeeze(nc_fid.variables['cssf'][:])
    label.ddde    = np.squeeze(nc_fid.variables['ddde'][:])
    label.dden    = np.squeeze(nc_fid.variables['dden'][:]) 

    label.lev     = np.squeeze(nc_fid.variables['lev'][:]) 


    #Transform  to date time 
    label.data   = num2date(label.time,units=nc_fid.variables['time'].units,calendar=nc_fid.variables['time'].calendar)


    #Pressure nivel 
    #Z=[1.000000, 0.989934, 0.974009, 0.954290, 0.930081, 0.900698, 0.865537, 0.824114, 0.776260, 0.722185, \
    #   0.662603, 0.598714, 0.532217, 0.465086, 0.399394, 0.337014, 0.279476, 0.227787, 0.182459, 0.143533, \
    #   0.110697, 0.083428, 0.061061, 0.042912, 0.028306, 0.016629, 0.007338, 0.003669]


    #tu = "days  since 2013-12-31T00:00:00 +04:00:00"
    #tc = "gregorian"
    #label.data       = num2date(label.time[:],units=tu,calendar=tc)

    return label 

#Experiment={
#            'clirad':variables, 
#            'clirad_hb':variables 
#           }

#print(Experiment['clirad.var1])



#time    = nc_fid.variables['time'][:]
#
#prec    = nc_fid.variables['prec'][:]  
#
#oces    = nc_fid.variables['oces'][:]  
#
#ocis    = nc_fid.variables['ocis'][:]  
#
#olis    = nc_fid.variables['olis'][:]  
#
#oles    = nc_fid.variables['oles'][:]  
#
#ocic    = nc_fid.variables['ocic'][:]  
#
#tsfc    = nc_fid.variables['tsfc'][:]  
#
#clsf    = nc_fid.variables['clsf'][:]  
#
#cssf    = nc_fid.variables['cssf'][:]  
#
#ddde    = nc_fid.variables['ddde'][:]  
#
#dden    = nc_fid.variables['dden'][:]  
