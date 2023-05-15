import  numpy       as     np

#Python standard library datetime  module
import datetime as dt


def diurnal_function_goa(time,variable,nh,hi): 

    #Number of hour
    ndh     = 24
#Hour array
    hour    = np.zeros(int(ndh/nh))
    #Sum variable to the mean 
    varsum   = np.zeros(int(ndh/nh))
    #Number of  time thar variable was sum 
    cont    = np.zeros(int(ndh/nh))

    
    #Lengh of the time array to search
    ndtp    = len(time) 
    

    conh=0

    #print(time[:])


    for i in range(0,ndtp):

        #print(time[i].hour, ndtp)
    
        conh=0

        for j in range(hi,ndh,nh):

            if int(time[i].hour)==j : 
    
                hour[conh]  = j
                varsum[conh]= varsum[conh]+variable[i]
                cont[conh]  = cont[conh]+1

            conh+=1
    
    meanvar = varsum/cont

    return meanvar,hour 

def diurnal_function(time,variable): 

    

#print timed.datetime.hour

    #Number of hour
    ndh     = 24
#Hour array
    hour    = np.zeros(ndh)
    #Sum variable to the mean 
    varsum   = np.zeros(ndh)
    #Number of  time thar variable was sum 
    cont    = np.zeros(ndh)

    
    #Lengh of the time array to search
    ndtp    = len(time) 
    

    #print(time[:])

    for i in range(0,ndtp):

        #print(time[i].hour, ndtp)
    
        for j in range(0,ndh):

            if int(time[i].hour)==j : 
    
                hour[j]=j
                varsum[j]=varsum[j]+variable[i]
                cont[j]=cont[j]+1

    
    meanvar = varsum/cont

    return meanvar,hour 

def diurnal_function_exp(time,variable): 

    #print timed.datetime.hour

    #Number of hour
    ndh     = 24
#Hour array
    hour    = np.zeros(ndh)
    #Sum variable to the mean 
    varsum   = np.zeros(ndh)
    #Number of  time thar variable was sum 
    cont    = np.zeros(ndh)
    
    #Lengh of the time array to search
    ndtp    = len(time) 

    #defaul time
    timebefore=dt.datetime(2000,1,1,0,0)
    
    for i in range(0,ndtp):
    
        for j in range(0,ndh):
    
            #to fund in an hour 
            if int(time[i].hour)==j: 

                hour[j]=j

                #to found in the half of an hour on time  
                if int(time[i].minute)<30: 

                    #to no stay in the same hour 
                    if int(time[i].hour)!=timebefore.hour: 

                        varsum[j]=varsum[j]+variable[i]
                        cont[j]=cont[j]+1

                        #print time[i]
                        timebefore=time[i] 

                        continue

                
    
    meanvar = varsum/cont


    return meanvar,hour 
