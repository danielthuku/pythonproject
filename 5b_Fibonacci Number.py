#Write a function to compute the nth Fibonacci number. A Fibonacci sequence is a sequence of numbers where each successive 
#number is the sum of the previous two. The classic Fibonacci sequence begins as 1, 1, 2, 3, 5, 8, 13, ...
#Then write a main program that prompts the user to enter n and prints out the nth Fibonacci number. For example, if the user 
#enters 6, then it should print out 8.

def main():
    
    print("This Program will Compute the nth Fibonacci Number")
    
    print ()
    
    a,b = 1,1
    
    num=eval(input("Enter Fibonacci number you want calculated: "))
    
    num_int=int(num-2)
    
    for i in range (num_int):
    
        a,b=b,a+b
    
    print ()
    
    print("The %sth Fibonacci number is : %s " % (num , b))
 
main()