import math

def main():
    print("This program finds the Area of the triangle")
    print() 

    a, b, c = eval(input("Please enter the length of the three sides of the triangle  (a, b, c): "))

    s= ((a + b + c) / 2)

      
    area = math.sqrt(s * (s-a) * (s-b)* (s-c))
    
    print("The Area of the triangle is:", area)

main()

