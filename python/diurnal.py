import  numpy       as     np

#Python standard library datetime  module
import datetime as dt


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
    

    print(time[:])

    for i in range(0,ndtp):

        print(time[i].hour, ndtp)
    
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
