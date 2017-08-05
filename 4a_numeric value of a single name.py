#Numerologists claim to be able to determine a person’s character traits based on the “numeric value” of a name. 
#The value of a name is determined by summing up the values of the letters of the name where “a” or “A” is 1, “b” or “B” is 2, and so on, 
#up to “z” or “Z” being 26. For example, the name “Zelle” would have the value 26 + 5 + 12 + 12 + 5 = 60.
#Write a program that calculates and prints out the numeric value of a single name provided as input by the user.


print ("This program will calculates and prints out the numeric value of a single name")
print()

#This function will count words 
def calcWordCount(name, value=0):
    
    for char in name:
        
        value += int(char, 36) - 9                     
    
    return (value)


#This function will get Single name e.g Zelle
def getName():
    
    name = input("Enter Single name: ").lower()
    
    return name

name = getName()


#This is the Main Function
def main():
    ans = calcWordCount(name)

    print ()

    print ("The 'numeric value' of %s is :  %s. " %  (name,ans))
    
main()    