import os.path

#convert string items to numbers
def toNumbers(nums):
    x = 0
    xz = 0
    notCounted = 0
    #for i in :
    i=0
    while i<len(nums):    
        try: 
            int(i)
            if (int(i) >= 0 ):
                nums[x]= int(nums[i])
                x = x+1
                i+=1
            else:
                nums.remove(nums[i])
                notCounted = notCounted + 1   
        except ValueError:
            nums.remove(nums[i])
            notCounted = notCounted + 1
         
            
    if notCounted > 0:
        print("")
        print("%s Value not were not counted Because; \nEither Empty or Wrong type. Please check your input file!\n" % str(notCounted))
    return   nums  
        
# Square All Numbers in a List     
def squareEach(vTonum):
    x = 0
    for i in vTonum:
        vTonum[x]= i**2
        x = x+1
    return vTonum    
#compute total sums of squared numbers 
def sumList(vsquareN):
    sum = 0
    for i in vsquareN:
        sum = sum+i
    return sum
     
# This function will  request filename input from the user e.g file.txt
def getFileName():
    goodinput = False
    while not goodinput:
        
        try:

            fname = input("Please enter filename: ")
            fileDir = os.path.dirname(os.path.realpath('__file__'))
            vfnamePath = os.path.abspath(fname) 
            if os.path.exists(vfnamePath):
                goodinput = True
                return vfnamePath, fname 
            else:
                print("Error: file not found Please Enter correct file name:!")
                print ("")
        except FileNotFoundError:
             print("Error: file not found Please Enter correct file name:!")
             print ("")
             
                  
     
def main():
    print('A program to read numbers from file, squaring and compute total sums.')
    print("")
    
    file , fname  = getFileName()
    print("")
     
    infile = open(file,'r')
 
    nums = []
    vnums = []
    
    i = infile.readline()
    nums = i.split()  
    print("This is the List on numbers from your file :  "  + str(nums))    
    

    vnums = toNumbers(nums) 
    print ("Converted List : " +  str(vnums))                
    vsquareN = squareEach(vnums)
    print ("Squared List : " + str(vsquareN))
    total = sumList(vsquareN)
    

    print('\nTotal sum of Squared numbers from file "{0}" is {1}.'.format(fname,total))
main()