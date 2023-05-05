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
    
    label.time    = nc_fid.variables['time'][:]  
    label.prec    = nc_fid.variables['prec'][:]  
    label.temp    = nc_fid.variables['temp'][:]  
    label.tsfc    = nc_fid.variables['tsfc'][:]  
    label.clsf    = nc_fid.variables['clsf'][:]  
    label.cssf    = nc_fid.variables['cssf'][:]  
    label.scvm    = nc_fid.variables['scvm'][:]  
    label.pblt    = nc_fid.variables['pblt'][:]  
    label.pblq    = nc_fid.variables['pblq'][:]  
    label.lglh    = nc_fid.variables['lglh'][:]  
    label.lgms    = nc_fid.variables['lgms'][:]  
    label.vdcc    = nc_fid.variables['vdcc'][:]  
    label.cvcl    = nc_fid.variables['cvcl'][:]  
    label.sscl    = nc_fid.variables['sscl'][:]  
    label.liqm    = nc_fid.variables['liqm'][:]  
    label.scvh    = nc_fid.variables['scvh'][:]  
    label.icem    = nc_fid.variables['icem'][:]  
    label.scld    = nc_fid.variables['scld'][:]  
    label.pblh    = nc_fid.variables['pblh'][:]  
    label.cape    = nc_fid.variables['cape'][:]  
    label.ddmd    = nc_fid.variables['ddmd'][:]  
    label.cine    = nc_fid.variables['cine'][:]  
    label.eqpt    = nc_fid.variables['eqpt'][:]  
    label.ddmu    = nc_fid.variables['ddmu'][:]  

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
