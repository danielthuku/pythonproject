#The greatest common divisor (GCD) of two values can be computed using Euclids algorithm. Starting with the values of n and m where n > m, 
#we repeatedly apply the formula: n, m=m, n%m (i.e., n is replaced by m, and m is replaced by n%m) 
#until m is 0. At that point, n is the GCD of the original n and m.


#Function to get correct input from user
def goodValue(message):
    goodinput = False
    while not goodinput:
        try:

            number = int(input(message))
     
            if number > 0:
                goodinput = True
                return number
            else:
                print()
                print("The number entered is not a positive whole number!")
        except ValueError:
            print()
            print ("The input entered is not a positive whole number!")
        except  TypeError:
            print()
            print ("The input entered is not a positive whole number!")
            

#Function to request user if to terminate program
def computerAnother(xClose):
    
    while xClose == False:
        
        doNext = (str(input("Compute another GCD (Y/N):"))).lower()
    
        if doNext == 'y' or doNext == 'yes' or doNext == 'n' or doNext == 'no':
            
            if doNext == 'y' or doNext == 'yes':
                xClose = False
                print()
                return xClose
            else:
                print()
                return True
        else:
            print()
            print("I did not understand your entry!")
            
        
        

def main():
    print('This Program will calculate greatest common divisor (GCD)')
    print()
    
    
    
    try:

        while True:
            
            a = goodValue("Enter the First positive whole number: ")
            b = goodValue("Enter a second positive whole number: ")
                
     
                 
            n = a
            m = b
                 
            t = min(a, b)
            
            # Keep looping until t divides both a & b evenly     
            while a % t != 0 or b % t != 0:
                t -= 1
            
            print()     
            print('The GCD of {} and {} is {}.'.format(a,b,t))

            print()
             
            #Check if user want to do another GCD
            xClose = False
            toClose = computerAnother(xClose)
            
            if  toClose == True:
                print()
                print ("Goodbye!")
                break
            
     
    except NameError:
        print('Please correct your input!')
    except SyntaxError:
        print('Please correct your input!')
    except:
        print('\nUnknow Error!')
         
if __name__ == '__main__': main()