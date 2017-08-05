#Function to get correct input from user (Odometer Reading)
def goodOdAndGasValue(legCount, message, vlastord):
    goodinputB = False
    while not goodinputB:
        try:
            vOdometer=''  
            vGas=''
            vOdometerAndvGas='  '
            vOdometerAndvGas = str(input(message))
            
            
            if (vOdometerAndvGas.strip()).find(' ') != -1:
                while '  ' in vOdometerAndvGas:
                    mystring = vOdometerAndvGas.replace('  ', ' ')
                vOdometer,vGas = vOdometerAndvGas.split()
            elif (len( vOdometerAndvGas.strip()) == 0):
                vOdometerAndvGas=''
                goodinputB = True
                return vOdometerAndvGas 
                
    
     
            if ((float(vOdometer) > -1 and ((float(vOdometer)>vlastord) or (vlastord == 0)) and float(vGas) > -1) or (vOdometerAndvGas == '') ):
                goodinputB = True
                return vOdometerAndvGas
            else:
                if (float(vOdometer)<vlastord):
                    print("Error, Current [Odometer] value cannot be less than previous Value!")
                print("Error, Please Enter correct [Odometer Gas] value.!\n")
        except ValueError:
            print ("Error, Please Enter correct[Odometer Gas] value!\n")
        except  TypeError:
            print ("Error, Please Enter correct[Odometer Gas] value!\n")
                        

def main():
    print('This Program Will Computes Fuel Efficiency of a Multi-leg Journey.\n')
 
 
    try:
        #Enter Odometer reading at the start of the Journey
        message = 'Please Enter the START Odometer and Gas Reading?\n\
To END Press Enter Key/Return Key!\n\nEnter Values and separate each value with space[Odometer Gas]:'
        legCount=0
        vlastord= 0
        vJouneyStart = goodOdAndGasValue(legCount, message, vlastord)
        vOdmRdStrt , vGasRdStrt = vJouneyStart.split()
        print("")
         
        # keep vodmRdStrt to calculate Total MPG for all trip
        oLast = float(vOdmRdStrt)         
        gLast = float(vGasRdStrt)  
        vlastord = float(vOdmRdStrt)           
        legCount = 1
        legMPG = []
         
        # Get Leg Details
        message = ('\nLeg #{}, Please Enter the current Odometer and Gas Reading? \n\
To END Press Enter Key/Return Key\nEnter Values and separate each data by space[Odometer Gas]:'.format(str(legCount)))
        vGetCurrentVal = goodOdAndGasValue(legCount,message, vlastord)

         
        while vGetCurrentVal !='':
 
            vSumOrd,vSumGas = vGetCurrentVal.split()
 
            vSumOrd = float(vSumOrd)
            vSumGas = float(vSumGas)                          
            
            #print(float(round((vSumOrd-oLast)/(gLast - vSumGas),2)))
            legMPG.append(float(round((vSumOrd-oLast)/(gLast - vSumGas),2)))
         
            oLast = float(vSumOrd)
            gLast = float(vSumGas)
            vlastord = float(vSumOrd)
             
            legCount = legCount+1
 
            message = ('\nLeg #{}, Please Enter the current Odometer and Gas Reading?\n\
To END Press Enter Key/Return Key\nEnter Values and separate each data by space[Odometer Gas]:'.format(str(legCount)))
            vGetCurrentVal = goodOdAndGasValue(legCount,  message, vlastord)
  

        if legCount > 1:
            print('\nYour fuel efficiency measurement:')
             
            #legCount must be at least 1
            for i in range(legCount-1):
                print('Leg#{} has rate  of {} MPG.'.format(i+1,legMPG[i]))
                 
            #when trip end calculate total MpG of whole trip
            print('\nYour Trip was  %sMiles, Total Fuel consumption was %sGallons \n Average Fuel consumption is %sMPG.' % (round((vSumOrd- float(vOdmRdStrt)),2) ,round((float(vGasRdStrt) - vSumGas),2), round((vSumOrd- float(vOdmRdStrt))/(float(vGasRdStrt) - vSumGas),2)))
        else:
            print('\nNo result.')
         
    except ValueError:
        print('\nPlease correct your Odometer and GAS Reading.')
    except:
        print('\nPlease correct your Odometer and GAS Reading.')
    
if __name__ =='__main__': main()