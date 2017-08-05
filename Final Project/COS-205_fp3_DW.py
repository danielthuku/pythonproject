# Function to check leapCheck
def leapYear(year):
    if year % 400 == 0:
         leapCheck = 1
    elif year % 100 == 0:
        leapCheck = 0
    elif year % 4 ==0:
        leapCheck = 1
    else:
        leapCheck = 0
         
    return leapCheck
     
     
 # Function to check only valid date is Entered    
def gooddateValue():
    goodinput = False
    while not goodinput:
        try:
 
            userDate = input('Please enter date in form of month/day/year (mm/dd/yyyy).')
            # split String into 3 var
            month,day,year = userDate.split('/')
             
            # convert String to Integer
            month = int(month)
            day = int(day)
            year = int(year)
                
                    
            month31 = [1,3,5,7,8,10,12]
            month30 = [4,6,9,11]
             
        
            #Check if month is 2/February.
            if month == 2 :
                if leapCheck == 1:
                    if day <= 29 and day >= 1:
                        dateCheck = 1                  
                    else:
                        dateCheck = 0
                if leapCheck == 0:
                    if day <= 28 and day >= 1:
                        dateCheck = 1  
                    else:
                        dateCheck = 0   
             
        
            # check if month is 31 days
            for i in month31:
                if i == month:
                    if day>=1 and day<=31:
                        dateCheck = 1
                    else:
                        dateCheck = 0   
                     
            # check if Month is 30days
            for i in month30:
                if i == month:
                    if day>=1 and day<=30:
                        dateCheck = 1
                    else:
                        dateCheck = 0       
         
            # in case user input silly month (below 1 or over 12)
            if month < 1:
                dateCheck = 0
            if month > 12:
                dateCheck = 0
             
            if (len(str(year)) == 4):
                year = int(year)
            else:
                dateCheck = 0   
 
            if dateCheck == 1:
                goodinput = True
                return dateCheck,month,day,year
            else:
                print("Error, The Date Entered is not Valid. Please try again!\n")
        except ValueError:
            print ("Error, The Date Entered is not Valid. Please try again!\n")
        except  TypeError:
            print ("Error, The Date Entered is not Valid. Please try again!\n")
 
 
def main():
     
    print('This Program will Compute Sequential Day of the Year.')
    print("")
 
    try:


        #Get a good date Entry from User
        dateCheck,month,day,year = gooddateValue()
        dateCheck = int(dateCheck)
        month= int(month)
        day= int(day)
        year= int(year)
 
        #check leap year so can use var later to check date count
        leapCheck = leapYear(year)
        

        if dateCheck == 1:
            dayNum = (31*(month-1))+day
             

            if month >= 3:
                dayNum = dayNum-((4*month)+23)//10
             

            if month >= 3 and leapCheck == 1 :
                dayNum = dayNum+1
                     
            print('\nDay of the Year is : ',dayNum)
         
    except ValueError:
        print('\nError, The Date Entered is not Valid. Please try again!')
    except:
        print('\nError, The Date Entered is not Valid. Please try again!')       
     
if __name__ == '__main__':
    main()