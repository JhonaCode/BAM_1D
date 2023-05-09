#Date to plot 

# Your files location

file_l = "#filenc#"  

file_o = "#figout#"  

#First day of the experiment 
#%%%%Y%%M%%D%%H
di="2014021500" 

#Inicial day 
#dayi       ="2011100101" 
dayi       ="2014021501" 
#Final day 
dayf       ="2014032500" 
#dayf       ="2011123100" 

#Hours interval 
step_hours = 1 

#Varible to plot 
# To know the name of the variables and 
# which are avalible see .clt

#number of variables to save 
nvtp=26 

##prec   0 99 total precipitation         (kg m**-2 day**-1)
var1="prec"
var1units="(kg m**-2 day**-1)"
nameplot1= "precipitation"


#TEMP  28 99 ABSOLUTE TEMPERATURE                    (K               )
var2="temp"
var2units="(K)"
nameplot2= "ABSOLUTE TEMPERATURE "

#TSFC   0 99 SURFACE TEMPERATURE                     (K               )
var3="tsfc"
var3units="(k)"
nameplot3= "surface temperature"

#clsf   0 99 latent heat flux from surface           (w m**-2         )
var4="clsf"
var4units="(w m**-2)"
nameplot4= "latent heat flux from surface"


#oces   0 99 net long wave at bottom       (w m**-2)
var5="oces"
var5units="(w m**-2)"
nameplot5= "oces"


#CSSF   0 99 SENSIBLE HEAT FLUX FROM SURFACE         (W M**-2         )
var6="cssf"
var6units="(w m**-2)"
nameplot6= "sensible heat flux from surface "

#SCVM   0 99 CLOUD COVER                             (No Dim          )
var7="scvm"
var7units="noDim"
nameplot7= "cloud cover"

#PBLT  28 99 CONVECTIVE LATENT HEATING               (K/Sec           )
var8="pblt"
var8units="K/sec"
nameplot8= "CONVECTIVE LATENT HEATING"

#PBLQ  28 99 CONVECTIVE MOISTURE SOURCE              (1/Sec           )
var9="pblq"
var9units="1/sec"
nameplot9= "CONVECTIVE MOISTURE SOURCE"

#LGLH  28 99 SHALLOW CONVECTIVE HEATING              (K/Sec           )
var10="lglh"
var10units="K/sec"
nameplot10= "SHALLOW CONVECTIVE HEATING"

#LGMS  28 99 SHALLOW CONV. MOISTURE SOURCE           (1/Sec           )
var11="lgms"
var11units="1/sec"
nameplot11= "SHALLOW CONV. MOISTURE SOURCE"

#VDCC  28 99 CONVECTIVE CLOUD                        (No Dim          )
var12="vdcc"
var12units="noDim"
nameplot12= "CONVECTIVE CLOUD"

#CVCL  28 99 SHALLOW CONVECTIVE CLOUD                (No Dim          )
var13="cvcl"
var13units="noDim"
nameplot13= "SHALLOW CONVECTIVE CLOUD"

#SSCL   0 99 PLANETARY BOUNDARY LAYER HEIGHT         (M               )
var14="sscl"
var14units="noDim"
nameplot14= "PLANETARY BOUNDARY LAYER HEIGHT"

#LIQM  28 99 LIQUID MIXING RATIO KG/KG               (No Dim          )
var15="liqm"
var15units="kg/kg"
nameplot15= "LIQUID MIXING RATIO KG/KG"

#SCVH  28 99 TURBULENT KINETIC ENERGY                (M/Sec           )
var16="scvh"
var16units="m/sec"
nameplot16= "TURBULENT KINETIC ENERGY"

#ICEM  28 99 ICE MIXING RATIO KG/KG                  (No Dim          )
var17="icem"
var17units="kg/kg"
nameplot17= "ICE MIXING RATIO"

#SCLD   0 99 CONVECTIVE AVAIL. POT.ENERGY            (M**2 Sec**-2    )
var18="scld"
var18units="M**2 Sec**-2"
nameplot18= "CONVECTIVE AVAIL. POT.ENERGY"

#PBLH   0 99 CONVECTIVE INHIB. ENERGY                (M**2 Sec**-2    )
var19="pblh"
var19units="M**2 Sec**-2"
nameplot19= "CONVECTIVE INHIB. ENERGY "

#CAPE  28 99 EQUIVALENT POTENTIAL TEMP               (No Dim          )
var20="cape"
var20units="nodim"
nameplot20= "EQUIVALENT POTENTIAL TEMP"

#DDMD  28 99 DEEP ENTRAINMENT                        (No Dim          )
var21="ddmd"
var21units="nodim"
nameplot21= "DEEP ENTRAINMENT"

#CINE  28 99 DEEP UPDRAFT MASS FLUX                  (No Dim          )
var22="cine"
var22units="nodim"
nameplot22= "DEEP UPDRAFT MASS FLUX"

#EQPT  28 99 DEEP DOWNDRAFT MASS FLUX                (No Dim          )
var23="eqpt"
var23units="nodim"
nameplot23= "DEEP UPDRAFT MASS FLUX"

#DDMU  28 99 DEEP DETRAINMENT                        (No Dim          )
var24="ddmu"
var24units="nodim"
nameplot24= "DEEP DETRAINMENT"

#DDDE  28 99 TEMPERATURE FORCING                     (No Dim          )
var25="dddn"
var25units="nodim"
nameplot25= "TEMPERATURE FORCING"

#DDEN  28 99 MOISTURE FORCING                        (No Dim          )
var26="dden"
var26units="nodim"
nameplot26= "MOISTURE FORCING"



