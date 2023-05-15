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

    def __init__(self):

        self.time   =   'time'
        self.lon    =   'lon'
        self.lat    =   'lat'
        self.lev    =   'lev'
        self.topo   =   'topo'
        self.lsmk   =   'lsmk'
        self.pslc   =   'pslc'
        self.divg   =   'divg'
        self.vort   =   'vort'
        self.umes   =   'umes'
        self.temp   =   'temp'
        self.uvel   =   'uvel'
        self.vvel   =   'vvel'
        self.zorl   =   'zorl'
        self.tsfc   =   'tsfc'
        self.td0s   =   'td0s'
        self.amdl   =   'amdl'
        self.amsl   =   'amsl'
        self.ussl   =   'ussl'
        self.uzrs   =   'uzrs'
        self.uzds   =   'uzds'
        self.prec   =   'prec'
        self.prcv   =   'prcv'
        self.neve   =   'neve'
        self.rnof   =   'rnof'
        self.pwat   =   'pwat'
        self.cssf   =   'cssf'
        self.clsf   =   'clsf'
        self.usst   =   'usst'
        self.vsst   =   'vsst'
        self.cbnv   =   'cbnv'
        self.olis   =   'olis'
        self.oles   =   'oles'
        self.role   =   'role'
        self.iswf   =   'iswf'
        self.ocis   =   'ocis'
        self.oces   =   'oces'
        self.roce   =   'roce'
        self.swea   =   'swea'
        self.ocas   =   'ocas'
        self.slds   =   'slds'
        self.lwrh   =   'lwrh'
        self.swrh   =   'swrh'
        self.lhcv   =   'lhcv'
        self.mscv   =   'mscv'
        self.lglh   =   'lglh'
        self.lgms   =   'lgms'
        self.scvh   =   'scvh'
        self.scvm   =   'scvm'
        self.pblt   =   'pblt'
        self.pblq   =   'pblq'
        self.gdsz   =   'gdsz'
        self.gdsm   =   'gdsm'
        self.gdtz   =   'gdtz'
        self.gdtm   =   'gdtm'
        self.olic   =   'olic'
        self.rolc   =   'rolc'
        self.ocic   =   'ocic'
        self.swgc   =   'swgc'
        self.swtc   =   'swtc'
        self.swec   =   'swec'
        self.ocac   =   'ocac'
        self.lwbc   =   'lwbc'
        self.vdcc   =   'vdcc'
        self.invc   =   'invc'
        self.sscl   =   'sscl'
        self.cvcl   =   'cvcl'
        self.scld   =   'scld'
        self.clwp   =   'clwp'
        self.emlw   =   'emlw'
        self.scop   =   'scop'
        self.pblh   =   'pblh'
        self.khpb   =   'khpb'
        self.kmpb   =   'kmpb'
        self.liqm   =   'liqm'
        self.tken   =   'tken'
        self.icem   =   'icem'
        self.cape   =   'cape'
        self.cine   =   'cine'
        self.eqpt   =   'eqpt'
        self.dden   =   'dden'
        self.ddmu   =   'ddmu'
        self.ddmd   =   'ddmd'
        self.ddde   =   'ddde'
        self.tmfc   =   'tmfc'
        self.mofc   =   'mofc'


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
    

    prec    = np.squeeze(nc_fid.variables['prec'][:]) 
    #prec to mm/hour
    rho_w   =  997.0 #[kg/m^3]
    #prec    = kg*m-2*day-1*1/rho_w*m^3/kg*1dia/24hour
    #        = 1/(24.0rho_w) [m/hour]*1000mm/1m
    label.prec     = 1000.0/(24.0*rho_w)*prec #[mm/hour]

    prcv         = np.squeeze(nc_fid.variables['prcv'][:])
    label.prcv   = 1000.0/(24.0*rho_w)*prcv

    label.lev    = np.squeeze(nc_fid.variables['lev'][:])  

    label.lon    = np.squeeze(nc_fid.variables['lon'])
    label.lat    = np.squeeze(nc_fid.variables['lat'])
    label.lev    = np.squeeze(nc_fid.variables['lev'])
    label.topo   = np.squeeze(nc_fid.variables['topo'])
    label.lsmk   = np.squeeze(nc_fid.variables['lsmk'])
    label.pslc   = np.squeeze(nc_fid.variables['pslc'])
    label.divg   = np.squeeze(nc_fid.variables['divg'])
    label.vort   = np.squeeze(nc_fid.variables['vort'])
    label.umes   = np.squeeze(nc_fid.variables['umes'])
    label.temp   = np.squeeze(nc_fid.variables['temp'])
    label.uvel   = np.squeeze(nc_fid.variables['uvel'])
    label.vvel   = np.squeeze(nc_fid.variables['vvel'])
    label.zorl   = np.squeeze(nc_fid.variables['zorl'])
    label.tsfc   = np.squeeze(nc_fid.variables['tsfc'])
    label.td0s   = np.squeeze(nc_fid.variables['td0s'])
    label.amdl   = np.squeeze(nc_fid.variables['amdl'])
    label.amsl   = np.squeeze(nc_fid.variables['amsl'])
    label.ussl   = np.squeeze(nc_fid.variables['ussl'])
    label.uzrs   = np.squeeze(nc_fid.variables['uzrs'])
    label.uzds   = np.squeeze(nc_fid.variables['uzds'])
    label.neve   = np.squeeze(nc_fid.variables['neve'])
    label.rnof   = np.squeeze(nc_fid.variables['rnof'])
    label.pwat   = np.squeeze(nc_fid.variables['pwat'])
    label.cssf   = np.squeeze(nc_fid.variables['cssf'])
    label.clsf   = np.squeeze(nc_fid.variables['clsf'])
    label.usst   = np.squeeze(nc_fid.variables['usst'])
    label.vsst   = np.squeeze(nc_fid.variables['vsst'])
    label.cbnv   = np.squeeze(nc_fid.variables['cbnv'])
    label.olis   = np.squeeze(nc_fid.variables['olis'])
    label.oles   = np.squeeze(nc_fid.variables['oles'])
    label.role   = np.squeeze(nc_fid.variables['role'])
    label.iswf   = np.squeeze(nc_fid.variables['iswf'])
    label.ocis   = np.squeeze(nc_fid.variables['ocis'])
    label.oces   = np.squeeze(nc_fid.variables['oces'])
    label.roce   = np.squeeze(nc_fid.variables['roce'])
    label.swea   = np.squeeze(nc_fid.variables['swea'])
    label.ocas   = np.squeeze(nc_fid.variables['ocas'])
    label.slds   = np.squeeze(nc_fid.variables['slds'])
    label.lwrh   = np.squeeze(nc_fid.variables['lwrh'])
    label.swrh   = np.squeeze(nc_fid.variables['swrh'])
    label.lhcv   = np.squeeze(nc_fid.variables['lhcv'])
    label.mscv   = np.squeeze(nc_fid.variables['mscv'])
    label.lglh   = np.squeeze(nc_fid.variables['lglh'])
    label.lgms   = np.squeeze(nc_fid.variables['lgms'])
    label.scvh   = np.squeeze(nc_fid.variables['scvh'])
    label.scvm   = np.squeeze(nc_fid.variables['scvm'])
    label.pblt   = np.squeeze(nc_fid.variables['pblt'])
    label.pblq   = np.squeeze(nc_fid.variables['pblq'])
    label.gdsz   = np.squeeze(nc_fid.variables['gdsz'])
    label.gdsm   = np.squeeze(nc_fid.variables['gdsm'])
    label.gdtz   = np.squeeze(nc_fid.variables['gdtz'])
    label.gdtm   = np.squeeze(nc_fid.variables['gdtm'])
    label.olic   = np.squeeze(nc_fid.variables['olic'])
    label.rolc   = np.squeeze(nc_fid.variables['rolc'])
    label.ocic   = np.squeeze(nc_fid.variables['ocic'])
    label.swgc   = np.squeeze(nc_fid.variables['swgc'])
    label.swtc   = np.squeeze(nc_fid.variables['swtc'])
    label.swec   = np.squeeze(nc_fid.variables['swec'])
    label.ocac   = np.squeeze(nc_fid.variables['ocac'])
    label.lwbc   = np.squeeze(nc_fid.variables['lwbc'])
    label.vdcc   = np.squeeze(nc_fid.variables['vdcc'])
    label.invc   = np.squeeze(nc_fid.variables['invc'])
    label.sscl   = np.squeeze(nc_fid.variables['sscl'])
    label.cvcl   = np.squeeze(nc_fid.variables['cvcl'])
    label.scld   = np.squeeze(nc_fid.variables['scld'])
    label.clwp   = np.squeeze(nc_fid.variables['clwp'])
    label.emlw   = np.squeeze(nc_fid.variables['emlw'])
    label.scop   = np.squeeze(nc_fid.variables['scop'])
    label.pblh   = np.squeeze(nc_fid.variables['pblh'])
    label.khpb   = np.squeeze(nc_fid.variables['khpb'])
    label.kmpb   = np.squeeze(nc_fid.variables['kmpb'])
    label.liqm   = np.squeeze(nc_fid.variables['liqm'])
    label.tken   = np.squeeze(nc_fid.variables['tken'])
    label.icem   = np.squeeze(nc_fid.variables['icem'])
    label.cape   = np.squeeze(nc_fid.variables['cape'])
    label.cine   = np.squeeze(nc_fid.variables['cine'])
    label.eqpt   = np.squeeze(nc_fid.variables['eqpt'])
    label.dden   = np.squeeze(nc_fid.variables['dden'])
    label.ddmu   = np.squeeze(nc_fid.variables['ddmu'])
    label.ddmd   = np.squeeze(nc_fid.variables['ddmd'])
    label.ddde   = np.squeeze(nc_fid.variables['ddde'])
    label.tmfc   = np.squeeze(nc_fid.variables['tmfc'])
    label.mofc   = np.squeeze(nc_fid.variables['mofc'])


    #Transform  to date time 
    #label.data   = num2date(label.time,units=nc_fid.variables['time'].units,calendar=nc_fid.variables['time'].calendar)
    #print(nc_fid.variables['time'].units)

    tu = "hours  since 2014-02-15T00:00:00 +04:00:00"
    tc = "standard"
    label.data       = num2date(label.time[:],units=tu,calendar=tc)

    return label 

	#double time(time) ;
	#	time:standard_name = "time" ;
	#	time:units = "hours since 2014-2-15 00:00:00" ;
	#	time:calendar = "standard" ;
	#	time:axis = "T" ;
	#double lon(lon) ;
	#	lon:standard_name = "longitude" ;
	#	lon:long_name = "longitude" ;
	#	lon:units = "degrees_east" ;
	#	lon:axis = "X" ;
	#double lat(lat) ;
	#	lat:standard_name = "latitude" ;
	#	lat:long_name = "latitude" ;
	#	lat:units = "degrees_north" ;
	#	lat:axis = "Y" ;
	#double lev(lev) ;
	#	lev:axis = "Z" ;
	#float topo(time, lat, lon) ;
	#	topo:long_name = "TOPOGRAPHY                              (M               )" ;
	#	topo:_FillValue = -2.56e+33f ;
	#	topo:missing_value = -2.56e+33f ;
	#float lsmk(time, lat, lon) ;
	#	lsmk:long_name = "LAND SEA MASK                           (NO DIM          )" ;
	#	lsmk:_FillValue = -2.56e+33f ;
	#	lsmk:missing_value = -2.56e+33f ;
	#float pslc(time, lat, lon) ;
	#	pslc:long_name = "SURFACE PRESSURE                        (Mb              )" ;
	#	pslc:_FillValue = -2.56e+33f ;
	#	pslc:missing_value = -2.56e+33f ;
	#float divg(time, lev, lat, lon) ;
	#	divg:long_name = "DIVERGENCE                              (1/Sec           )" ;
	#	divg:_FillValue = -2.56e+33f ;
	#	divg:missing_value = -2.56e+33f ;
	#float vort(time, lev, lat, lon) ;
	#	vort:long_name = "VORTICITY                               (1/Sec           )" ;
	#	vort:_FillValue = -2.56e+33f ;
	#	vort:missing_value = -2.56e+33f ;
	#float umes(time, lev, lat, lon) ;
	#	umes:long_name = "SPECIFIC HUMIDITY                       (No Dim          )" ;
	#	umes:_FillValue = -2.56e+33f ;
	#	umes:missing_value = -2.56e+33f ;
	#float temp(time, lev, lat, lon) ;
	#	temp:long_name = "ABSOLUTE TEMPERATURE                    (K               )" ;
	#	temp:_FillValue = -2.56e+33f ;
	#	temp:missing_value = -2.56e+33f ;
	#float uvel(time, lev, lat, lon) ;
	#	uvel:long_name = "ZONAL WIND                              (m/Sec           )" ;
	#	uvel:_FillValue = -2.56e+33f ;
	#	uvel:missing_value = -2.56e+33f ;
	#float vvel(time, lev, lat, lon) ;
	#	vvel:long_name = "MERIDIONAL WIND                         (m/Sec           )" ;
	#	vvel:_FillValue = -2.56e+33f ;
	#	vvel:missing_value = -2.56e+33f ;
	#float zorl(time, lat, lon) ;
	#	zorl:long_name = "ROUGHNESS LENGTH                        (M               )" ;
	#	zorl:_FillValue = -2.56e+33f ;
	#	zorl:missing_value = -2.56e+33f ;
	#float tsfc(time, lat, lon) ;
	#	tsfc:long_name = "SURFACE TEMPERATURE                     (K               )" ;
	#	tsfc:_FillValue = -2.56e+33f ;
	#	tsfc:missing_value = -2.56e+33f ;
	#float td0s(time, lat, lon) ;
	#	td0s:long_name = "deep soil temperature                   (K               )" ;
	#	td0s:_FillValue = -2.56e+33f ;
	#	td0s:missing_value = -2.56e+33f ;
	#float amdl(time, lat, lon) ;
	#	amdl:long_name = "STORAGE ON CANOPY                       (M               )" ;
	#	amdl:_FillValue = -2.56e+33f ;
	#	amdl:missing_value = -2.56e+33f ;
	#float amsl(time, lat, lon) ;
	#	amsl:long_name = "STORAGE ON GROUND                       (M               )" ;
	#	amsl:_FillValue = -2.56e+33f ;
	#	amsl:missing_value = -2.56e+33f ;
	#float ussl(time, lat, lon) ;
	#	ussl:long_name = "SOIL WETNESS OF SURFACE                 (No Dim          )" ;
	#	ussl:_FillValue = -2.56e+33f ;
	#	ussl:missing_value = -2.56e+33f ;
	#float uzrs(time, lat, lon) ;
	#	uzrs:long_name = "SOIL WETNESS OF ROOT ZONE               (No Dim          )" ;
	#	uzrs:_FillValue = -2.56e+33f ;
	#	uzrs:missing_value = -2.56e+33f ;
	#float uzds(time, lat, lon) ;
	#	uzds:long_name = "SOIL WETNESS OF DRAINAGE ZONE           (No Dim          )" ;
	#	uzds:_FillValue = -2.56e+33f ;
	#	uzds:missing_value = -2.56e+33f ;
	#float prec(time, lat, lon) ;
	#	prec:long_name = "TOTAL PRECIPITATION                     (Kg M**-2 Day**-1)" ;
	#	prec:_FillValue = -2.56e+33f ;
	#	prec:missing_value = -2.56e+33f ;
	#float prcv(time, lat, lon) ;
	#	prcv:long_name = "CONVECTIVE PRECIPITATION                (Kg M**-2 Day**-1)" ;
	#	prcv:_FillValue = -2.56e+33f ;
	#	prcv:missing_value = -2.56e+33f ;
	#float neve(time, lat, lon) ;
	#	neve:long_name = "SNOWFALL                                (Kg M**-2 Day**-1)" ;
	#	neve:_FillValue = -2.56e+33f ;
	#	neve:missing_value = -2.56e+33f ;
	#float rnof(time, lat, lon) ;
	#	rnof:long_name = "RUNOFF                                  (Kg M**-2 Day**-1)" ;
	#	rnof:_FillValue = -2.56e+33f ;
	#	rnof:missing_value = -2.56e+33f ;
	#float pwat(time, lat, lon) ;
	#	pwat:long_name = "PRECIPITABLE WATER                      (Kg M**-2        )" ;
	#	pwat:_FillValue = -2.56e+33f ;
	#	pwat:missing_value = -2.56e+33f ;
	#float cssf(time, lat, lon) ;
	#	cssf:long_name = "SENSIBLE HEAT FLUX FROM SURFACE         (W M**-2         )" ;
	#	cssf:_FillValue = -2.56e+33f ;
	#	cssf:missing_value = -2.56e+33f ;
	#float clsf(time, lat, lon) ;
	#	clsf:long_name = "LATENT HEAT FLUX FROM SURFACE           (W M**-2         )" ;
	#	clsf:_FillValue = -2.56e+33f ;
	#	clsf:missing_value = -2.56e+33f ;
	#float usst(time, lat, lon) ;
	#	usst:long_name = "SURFACE ZONAL WIND STRESS               (Pa              )" ;
	#	usst:_FillValue = -2.56e+33f ;
	#	usst:missing_value = -2.56e+33f ;
	#float vsst(time, lat, lon) ;
	#	vsst:long_name = "SURFACE MERIDIONAL WIND STRESS          (Pa              )" ;
	#	vsst:_FillValue = -2.56e+33f ;
	#	vsst:missing_value = -2.56e+33f ;
	#float cbnv(time, lat, lon) ;
	#	cbnv:long_name = "CLOUD COVER                             (No Dim          )" ;
	#	cbnv:_FillValue = -2.56e+33f ;
	#	cbnv:missing_value = -2.56e+33f ;
	#float olis(time, lat, lon) ;
	#	olis:long_name = "DOWNWARD LONG WAVE AT BOTTOM            (W M**-2         )" ;
	#	olis:_FillValue = -2.56e+33f ;
	#	olis:missing_value = -2.56e+33f ;
	#float oles(time, lat, lon) ;
	#	oles:long_name = "UPWARD LONG WAVE AT BOTTOM              (W M**-2         )" ;
	#	oles:_FillValue = -2.56e+33f ;
	#	oles:missing_value = -2.56e+33f ;
	#float role(time, lat, lon) ;
	#	role:long_name = "OUTGOING LONG WAVE AT TOP               (W M**-2         )" ;
	#	role:_FillValue = -2.56e+33f ;
	#	role:missing_value = -2.56e+33f ;
	#float iswf(time, lat, lon) ;
	#	iswf:long_name = "INCIDENT SHORT WAVE FLUX                (W M**-2         )" ;
	#	iswf:_FillValue = -2.56e+33f ;
	#	iswf:missing_value = -2.56e+33f ;
	#float ocis(time, lat, lon) ;
	#	ocis:long_name = "DOWNWARD SHORT WAVE AT GROUND           (W M**-2         )" ;
	#	ocis:_FillValue = -2.56e+33f ;
	#	ocis:missing_value = -2.56e+33f ;
	#float oces(time, lat, lon) ;
	#	oces:long_name = "UPWARD SHORT WAVE AT GROUND             (W M**-2         )" ;
	#	oces:_FillValue = -2.56e+33f ;
	#	oces:missing_value = -2.56e+33f ;
	#float roce(time, lat, lon) ;
	#	roce:long_name = "UPWARD SHORT WAVE AT TOP                (W M**-2         )" ;
	#	roce:_FillValue = -2.56e+33f ;
	#	roce:missing_value = -2.56e+33f ;
	#float swea(time, lat, lon) ;
	#	swea:long_name = "SHORT WAVE ABSORBED BY EARTH/ATMOSPHERE (W M**-2         )" ;
	#	swea:_FillValue = -2.56e+33f ;
	#	swea:missing_value = -2.56e+33f ;
	#float ocas(time, lat, lon) ;
	#	ocas:long_name = "SHORT WAVE ABSORBED AT GROUND           (W M**-2         )" ;
	#	ocas:_FillValue = -2.56e+33f ;
	#	ocas:missing_value = -2.56e+33f ;
	#float slds(time, lat, lon) ;
	#	slds:long_name = "NET LONG WAVE AT BOTTOM                 (W M**-2         )" ;
	#	slds:_FillValue = -2.56e+33f ;
	#	slds:missing_value = -2.56e+33f ;
	#float lwrh(time, lev, lat, lon) ;
	#	lwrh:long_name = "LONG WAVE RADIATIVE HEATING             (K/Sec           )" ;
	#	lwrh:_FillValue = -2.56e+33f ;
	#	lwrh:missing_value = -2.56e+33f ;
	#float swrh(time, lev, lat, lon) ;
	#	swrh:long_name = "SHORT WAVE RADIATIVE HEATING            (K/Sec           )" ;
	#	swrh:_FillValue = -2.56e+33f ;
	#	swrh:missing_value = -2.56e+33f ;
	#float lhcv(time, lev, lat, lon) ;
	#	lhcv:long_name = "CONVECTIVE LATENT HEATING               (K/Sec           )" ;
	#	lhcv:_FillValue = -2.56e+33f ;
	#	lhcv:missing_value = -2.56e+33f ;
	#float mscv(time, lev, lat, lon) ;
	#	mscv:long_name = "CONVECTIVE MOISTURE SOURCE              (1/Sec           )" ;
	#	mscv:_FillValue = -2.56e+33f ;
	#	mscv:missing_value = -2.56e+33f ;
	#float lglh(time, lev, lat, lon) ;
	#	lglh:long_name = "LARGE SCALE LATENT HEATING              (K/Sec           )" ;
	#	lglh:_FillValue = -2.56e+33f ;
	#	lglh:missing_value = -2.56e+33f ;
	#float lgms(time, lev, lat, lon) ;
	#	lgms:long_name = "LARGE SCALE MOISTURE SOURCE             (1/Sec           )" ;
	#	lgms:_FillValue = -2.56e+33f ;
	#	lgms:missing_value = -2.56e+33f ;
	#float scvh(time, lev, lat, lon) ;
	#	scvh:long_name = "SHALLOW CONVECTIVE HEATING              (K/Sec           )" ;
	#	scvh:_FillValue = -2.56e+33f ;
	#	scvh:missing_value = -2.56e+33f ;
	#float scvm(time, lev, lat, lon) ;
	#	scvm:long_name = "SHALLOW CONV. MOISTURE SOURCE           (1/Sec           )" ;
	#	scvm:_FillValue = -2.56e+33f ;
	#	scvm:missing_value = -2.56e+33f ;
	#float pblt(time, lev, lat, lon) ;
	#	pblt:long_name = "VERTICAL DIFFUSION HEATING              (K/Sec           )" ;
	#	pblt:_FillValue = -2.56e+33f ;
	#	pblt:missing_value = -2.56e+33f ;
	#float pblq(time, lev, lat, lon) ;
	#	pblq:long_name = "VERTICAL DIFF. MOISTURE SOURCE          (1/Sec           )" ;
	#	pblq:_FillValue = -2.56e+33f ;
	#	pblq:missing_value = -2.56e+33f ;
	#float gdsz(time, lat, lon) ;
	#	gdsz:long_name = "GRAVITY WAVE DRAG SFC ZONAL STRESS      (Pa              )" ;
	#	gdsz:_FillValue = -2.56e+33f ;
	#	gdsz:missing_value = -2.56e+33f ;
	#float gdsm(time, lat, lon) ;
	#	gdsm:long_name = "GRAVITY WAVE DRAG SFC MERIDIONAL STRESS (Pa              )" ;
	#	gdsm:_FillValue = -2.56e+33f ;
	#	gdsm:missing_value = -2.56e+33f ;
	#float gdtz(time, lev, lat, lon) ;
	#	gdtz:long_name = "GRAVITY WAVE DRAG DU/DT                 (M Sec**-2       )" ;
	#	gdtz:_FillValue = -2.56e+33f ;
	#	gdtz:missing_value = -2.56e+33f ;
	#float gdtm(time, lev, lat, lon) ;
	#	gdtm:long_name = "GRAVITY WAVE DRAG DV/DT                 (M Sec**-2       )" ;
	#	gdtm:_FillValue = -2.56e+33f ;
	#	gdtm:missing_value = -2.56e+33f ;
	#float olic(time, lat, lon) ;
	#	olic:long_name = "DOWNWARD LONG WAVE AT BOTTOM (CLEAR)    (W M**-2         )" ;
	#	olic:_FillValue = -2.56e+33f ;
	#	olic:missing_value = -2.56e+33f ;
	#float rolc(time, lat, lon) ;
	#	rolc:long_name = "OUTGOING LONG WAVE AT TOP (CLEAR)       (W M**-2         )" ;
	#	rolc:_FillValue = -2.56e+33f ;
	#	rolc:missing_value = -2.56e+33f ;
	#float ocic(time, lat, lon) ;
	#	ocic:long_name = "DOWNWARD SHORT WAVE AT GROUND (CLEAR)   (W M**-2         )" ;
	#	ocic:_FillValue = -2.56e+33f ;
	#	ocic:missing_value = -2.56e+33f ;
	#float swgc(time, lat, lon) ;
	#	swgc:long_name = "UPWARD SHORT WAVE AT GROUND (CLEAR)     (W M**-2         )" ;
	#	swgc:_FillValue = -2.56e+33f ;
	#	swgc:missing_value = -2.56e+33f ;
	#float swtc(time, lat, lon) ;
	#	swtc:long_name = "UPWARD SHORT WAVE AT TOP (CLEAR)        (W M**-2         )" ;
	#	swtc:_FillValue = -2.56e+33f ;
	#	swtc:missing_value = -2.56e+33f ;
	#float swec(time, lat, lon) ;
	#	swec:long_name = "SHORT WV ABSRBD BY EARTH/ATMOS (CLEAR)  (W M**-2         )" ;
	#	swec:_FillValue = -2.56e+33f ;
	#	swec:missing_value = -2.56e+33f ;
	#float ocac(time, lat, lon) ;
	#	ocac:long_name = "SHORT WAVE ABSORBED AT GROUND (CLEAR)   (W M**-2         )" ;
	#	ocac:_FillValue = -2.56e+33f ;
	#	ocac:missing_value = -2.56e+33f ;
	#float lwbc(time, lat, lon) ;
	#	lwbc:long_name = "NET LONG WAVE AT BOTTOM (CLEAR)         (W M**-2         )" ;
	#	lwbc:_FillValue = -2.56e+33f ;
	#	lwbc:missing_value = -2.56e+33f ;
	#float vdcc(time, lev, lat, lon) ;
	#	vdcc:long_name = "VERTICAL DIST TOTAL CLOUD COVER         (No Dim          )" ;
	#	vdcc:_FillValue = -2.56e+33f ;
	#	vdcc:missing_value = -2.56e+33f ;
	#float invc(time, lev, lat, lon) ;
	#	invc:long_name = "INVERSION CLOUD                         (No Dim          )" ;
	#	invc:_FillValue = -2.56e+33f ;
	#	invc:missing_value = -2.56e+33f ;
	#float sscl(time, lev, lat, lon) ;
	#	sscl:long_name = "SUPERSATURATION CLOUD                   (No Dim          )" ;
	#	sscl:_FillValue = -2.56e+33f ;
	#	sscl:missing_value = -2.56e+33f ;
	#float cvcl(time, lev, lat, lon) ;
	#	cvcl:long_name = "CONVECTIVE CLOUD                        (No Dim          )" ;
	#	cvcl:_FillValue = -2.56e+33f ;
	#	cvcl:missing_value = -2.56e+33f ;
	#float scld(time, lev, lat, lon) ;
	#	scld:long_name = "SHALLOW CONVECTIVE CLOUD                (No Dim          )" ;
	#	scld:_FillValue = -2.56e+33f ;
	#	scld:missing_value = -2.56e+33f ;
	#float clwp(time, lev, lat, lon) ;
	#	clwp:long_name = "CLOUD LIQUID WATER PATH                 (No Dim          )" ;
	#	clwp:_FillValue = -2.56e+33f ;
	#	clwp:missing_value = -2.56e+33f ;
	#float emlw(time, lev, lat, lon) ;
	#	emlw:long_name = "LONGWAVE CLOUD EMISSIVITY               (No Dim          )" ;
	#	emlw:_FillValue = -2.56e+33f ;
	#	emlw:missing_value = -2.56e+33f ;
	#float scop(time, lev, lat, lon) ;
	#	scop:long_name = "SHORTWAVE CLOUD OPTICAL DEPTH           (No Dim          )" ;
	#	scop:_FillValue = -2.56e+33f ;
	#	scop:missing_value = -2.56e+33f ;
	#float pblh(time, lat, lon) ;
	#	pblh:long_name = "PLANETARY BOUNDARY LAYER HEIGHT         (M               )" ;
	#	pblh:_FillValue = -2.56e+33f ;
	#	pblh:missing_value = -2.56e+33f ;
	#float khpb(time, lev, lat, lon) ;
	#	khpb:long_name = "DIFFUSION COEFFICIENT FOR HEAT          (M**2/Sec        )" ;
	#	khpb:_FillValue = -2.56e+33f ;
	#	khpb:missing_value = -2.56e+33f ;
	#float kmpb(time, lev, lat, lon) ;
	#	kmpb:long_name = "DIFFUSION COEFFICIENT FOR MOMENTUM      (M**2/Sec        )" ;
	#	kmpb:_FillValue = -2.56e+33f ;
	#	kmpb:missing_value = -2.56e+33f ;
	#float liqm(time, lev, lat, lon) ;
	#	liqm:long_name = "LIQUID MIXING RATIO KG/KG               (No Dim          )" ;
	#	liqm:_FillValue = -2.56e+33f ;
	#	liqm:missing_value = -2.56e+33f ;
	#float tken(time, lev, lat, lon) ;
	#	tken:long_name = "TURBULENT KINETIC ENERGY                (M/Sec           )" ;
	#	tken:_FillValue = -2.56e+33f ;
	#	tken:missing_value = -2.56e+33f ;
	#float icem(time, lev, lat, lon) ;
	#	icem:long_name = "ICE MIXING RATIO KG/KG                  (No Dim          )" ;
	#	icem:_FillValue = -2.56e+33f ;
	#	icem:missing_value = -2.56e+33f ;
	#float cape(time, lat, lon) ;
	#	cape:long_name = "CONVECTIVE AVAIL. POT.ENERGY            (M**2 Sec**-2    )" ;
	#	cape:_FillValue = -2.56e+33f ;
	#	cape:missing_value = -2.56e+33f ;
	#float cine(time, lat, lon) ;
	#	cine:long_name = "CONVECTIVE INHIB. ENERGY                (M**2 Sec**-2    )" ;
	#	cine:_FillValue = -2.56e+33f ;
	#	cine:missing_value = -2.56e+33f ;
	#float eqpt(time, lev, lat, lon) ;
	#	eqpt:long_name = "EQUIVALENT POTENTIAL TEMP               (No Dim          )" ;
	#	eqpt:_FillValue = -2.56e+33f ;
	#	eqpt:missing_value = -2.56e+33f ;
	#float dden(time, lev, lat, lon) ;
	#	dden:long_name = "DEEP ENTRAINMENT                        (No Dim          )" ;
	#	dden:_FillValue = -2.56e+33f ;
	#	dden:missing_value = -2.56e+33f ;
	#float ddmu(time, lev, lat, lon) ;
	#	ddmu:long_name = "DEEP UPDRAFT MASS FLUX                  (No Dim          )" ;
	#	ddmu:_FillValue = -2.56e+33f ;
	#	ddmu:missing_value = -2.56e+33f ;
	#float ddmd(time, lev, lat, lon) ;
	#	ddmd:long_name = "DEEP DOWNDRAFT MASS FLUX                (No Dim          )" ;
	#	ddmd:_FillValue = -2.56e+33f ;
	#	ddmd:missing_value = -2.56e+33f ;
	#float ddde(time, lev, lat, lon) ;
	#	ddde:long_name = "DEEP DETRAINMENT                        (No Dim          )" ;
	#	ddde:_FillValue = -2.56e+33f ;
	#	ddde:missing_value = -2.56e+33f ;
	#float tmfc(time, lev, lat, lon) ;
	#	tmfc:long_name = "TEMPERATURE FORCING                     (No Dim          )" ;
	#	tmfc:_FillValue = -2.56e+33f ;
	#	tmfc:missing_value = -2.56e+33f ;
	#float mofc(time, lev, lat, lon) ;
	#	mofc:long_name = "MOISTURE FORCING                        (No Dim          )" ;
	#	mofc:_FillValue = -2.56e+33f ;
	#	mofc:missing_value = -2.56e+33f ;
