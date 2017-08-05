#The speeding ticket fine policy in Podunskville is $50 plus $5 for each mph over the speed limit plus a penalty of $200 for any speed over 90 mph.
#Write a program that accepts a speed limit and a clocked speed from the user, and either prints a message indicating the speed was legal or prints the amount of the fine, if the speed was illegal.

def main():

    print("This Program will Calculate Legal or Illegal speed fine based on user input")
    print()
    
    # Get the driver's speed and limit
    drivers_speed = eval(input("Please enter the driver's speed: "))
    speed_limit = eval(input("Please enter the speed limit: "))
    
    # Compare the driver's speed with the limit
    if drivers_speed <= speed_limit:
        print()
        print("You are within the Legal speed Limit.")
    else:
        
        print()
        print("Your speed was %s mph which is above the Legal Limit of %s mph. " % (drivers_speed , speed_limit))
        
        speed_above =  drivers_speed - speed_limit
        print()
        print ("Your speed was above legal limit by %s mph." % str(speed_above ))        
        
        # Calculate the fine
        fine = 5.0 * (speed_above)
        
        
        
        if drivers_speed > 90:
            fine += 200
        print()   
        print("Please pay a fine of ${0:5.2f} for this offence!".format(fine))

if __name__ == "__main__":
    main()
