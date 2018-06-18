#    Circumcircle_user.py
#    A function to compute the output of a triangles semiperimeter
#    Matthew Shaw
#    Sunday, 4 October 2015 14:59:14

from math import sqrt
def circumcircle(side_a, side_b, side_c):



    semiperimiter = (side_a + side_b + side_c)/2



    diameter = (side_a* side_b* side_c)/ 2*sqrt(semiperimiter * (semiperimiter - side_a) * (semiperimiter - side_b) * (semiperimiter - side_c))
    
    return diameter
    

    

side_a = float(input("Please enter the value for side a:\t"))
side_b = float(input("Please enter the value for side b:\t"))
side_c = float(input('Please enter the value for side c:\t'))



diameter = circumcircle(side_a, side_b, side_c)     #allows acces to the variable
                                                    #outside the scope of the fucntion                                                   
    
radius = diameter/2
print
print ("The radius of a circle with sides of length", side_a ," ", side_b, " and ", side_c, " is", radius)
