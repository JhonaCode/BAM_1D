################################################# 
# Program to read variable of a nc file 
# using python with NetCdf
# Create by: Jhonatan Aguirre 
# Date:06/02/2020
# working:yes
#################################################

# Python module to read the information of the date
#from    Ncdump     import * 

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
    
    label.temp    = nc_fid.variables['temp'][:]  

    label.oces    = nc_fid.variables['oces'][:]  

    label.ocis    = nc_fid.variables['ocis'][:]  

    label.olis    = nc_fid.variables['olis'][:]  

    label.oles    = nc_fid.variables['oles'][:]  

    label.ocic    = nc_fid.variables['ocic'][:]  

    label.tsfc    = nc_fid.variables['tsfc'][:]  

    label.clsf    = nc_fid.variables['clsf'][:]  

    label.cssf    = nc_fid.variables['cssf'][:]  

    label.ddde    = nc_fid.variables['ddde'][:]  

    label.dden    = nc_fid.variables['dden'][:]  

    #Transform  to date time 
    label.data   = num2date(label.time,units=nc_fid.variables['time'].units,calendar=nc_fid.variables['time'].calendar)


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
