#Date to plot 

# Your files location

file_l = "#filenc#"  
file_outnc = "#fileoutnc#"  

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
nvtp=19 

##prec   0 99 total precipitation         (kg m**-2 day**-1)
var1="prec"
var1units="(kg m**-2 day**-1)"
nameplot1= "precipitation"

#oces   0 99 net long wave at bottom       (w m**-2)
var2="oces"
var2units="(w m**-2)"
nameplot2= "oces"

#ocis   0 99 downward short wave at ground   (w m**-2 )
var3="ocis"
var3units="(w m**-2)"
nameplot3= "ocis"

#olis   0 99 upward short wave at top (clear) (w m**-2)
var4="olis"
var4units="(w m**-2)"
nameplot4= "olis"

#oles   0 99 upward short wave at top       (w m**-2 )
var5="oles"
var5units="(w m**-2)"
nameplot5= "ocic"

var6="ocic"
var6units="(w m**-2)"
nameplot6= "ocic"

##surf. air temperature
#var7="tsair"
#var7units="(k)"
#nameplot7= "surface air temperature"

#TSFC   0 99 SURFACE TEMPERATURE                     (K               )
var7="tsfc"
var7units="(k)"
nameplot7= "surface temperature"

#clsf   0 99 latent heat flux from surface           (w m**-2         )
var8="clsf"
var8units="(w m**-2)"
nameplot8= "latent heat flux from surface"

#cssf   0 99 sensible heat flux from surface         (w m**-2         )
var9="cssf"
var9units="(w m**-2)"
nameplot9= "sensible heat flux from surface "

#role   0 99 outgoing long wave at top               (w m**-2         )
var10="role"
var10units="(w m**-2)"
nameplot10= "outgoing long wave at top "

#ocas   0 99 incident short wave flux                (w m**-2         )
var11="ocas"
var11units="(w m**-2)"
nameplot11= "incident short wave flux "


#roce   0 99 upward short wave at ground             (w m**-2         )
var12="roce"
var12units="(w m**-2)"
nameplot12= "upward short wave at ground "

#slds   0 99 SHORT WAVE ABSORBED BY EARTH/ATMOSPHERE (W M**-2         )
var13="slds"
var13units="(W M**-2)"
nameplot13= "SHORT WAVE ABSORBED BY EARTH/ATMOSPHERE"

#SWEA   0 99 SHORT WAVE ABSORBED AT GROUND           (W M**-2         )
var14="swea"
var14units="(W M**-2)"
nameplot14= "SHORT WAVE ABSORBED AT GROUND"

#OCAC  28 99 LONG WAVE RADIATIVE HEATING             (K/Sec           )
var15="ocac"
var15units="(K/Sec)"
nameplot15= "LONG WAVE RADIATIVE HEATING"

#ISWF  28 99 SHORT WAVE RADIATIVE HEATING            (K/Sec           
var16="iswf"
var16units="(K/Sec)"
nameplot16= "SHORT WAVE RADIATIVE HEATING "

#TEMP  28 99 ABSOLUTE TEMPERATURE                    (K)  
var17="temp"
var17units="(K)"
nameplot17= "ABSOLUTE TEMPERATURE "

#TEMPERATURE FORCING  28 99 ABSOLUTE TEMPERATURE                    (K)  
var18="ddde"
var18units="(K)"
nameplot19= "ABSOLUTE TEMPERATURE "

#MOISTURE FORCING  28 99 ABSOLUTE TEMPERATURE                    (K)  
var19="dden"
var19units="(K)"
nameplot19= "ABSOLUTE TEMPERATURE "


