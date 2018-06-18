from math import sqrt

side_a = 4
side_b = 6
side_c = 3

semiperimiter = (side_a + side_b + side_c)/2



diameter = (side_a* side_b* side_c)/ 2*sqrt(semiperimiter * (semiperimiter - side_a) * (semiperimiter - side_b) * (semiperimiter - side_c))

print ('The radius of a circle with sides of length 4, 6 and 3 is', diameter/2)
