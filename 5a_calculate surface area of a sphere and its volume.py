#sphereArea (radius): It returns the surface area of a sphere having the given radius. The formula is A = 4 pr2.
#sphereVolume(radius): It returns the volume of a sphere having the given radius. The formula is V = (4/3) pr3.
#Then write a main program that uses these functions to compute the surface area and volume of a sphere given the radius. The program should prompt the user for the radius and then print out the surface area and volume.

def sphereArea(radius):
    rad=radius*radius
  
    area=4*3.14*rad
    
    return area
  
def sphereVolume(radius):
    rad=radius*radius*radius
    
    volume=(4/3)*3.14*rad
    
    return volume
  

    
def main():
    print("This program will calculate surface area of a sphere and it's volume ")
    print()
    
    r =eval(input("Please enter the radius of the Sphere: "))
    
    print()
    print("The area of Sphere is : " + str(sphereArea(r)))

    print()
    print("Volume of Sphere : " + str(sphereVolume(r)))
    

main()    