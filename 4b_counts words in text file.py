#Write a program that counts the number of words in a text file.
#It should consider anything that is separated by white space or new line on either side of a contiguous group of characters or character as a word.
#For example, if the input file contains: “This is a test file” (quotation marks not included in file), then the program should print out: The input file contains 5 words.
#Your program should prompt the user for the file name, which should be stored at the same location as the program.


import os

print ("This program will counts the number of words in a text file")
print()

# This function will  request filename input from the user e.g file.txt
def getFileName():
    
    fname = input("Enter filename: ")

    fileDir = os.path.dirname(os.path.realpath('__file__'))

    fname = os.path.abspath(fname) 

    return fname


# This the Main function
def main():
    
    myfile    = open(getFileName())

    wordsCount = 0
    
    for lines in myfile:

        for words in lines.split():
            wordsCount += 1

    
    print()
    
    print ("The input file contains %s words." % wordsCount)

main()