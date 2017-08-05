
def main():
   
    print("This program computes the interest accrued on an account")
    
    
    principal = eval(input("Enter the initial principal: "))
    yearly_rate = eval(input("Enter the yearly interest rate as a decimal number."))
    periods_per_year = eval(input("Enter the the number of compounding periods in a year."))
    duration = eval(input("Enter Duration."))
    loopCnt = 10 * periods_per_year
    
    for i in range(loopCnt):
        
        principal = principal * (1 + (yearly_rate / periods_per_year))
    print("The value in 10 years is:", round(principal, 2))
    
main()      