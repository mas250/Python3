#quadratic solver

from math import sqrt

a = 1
b = -6
c = -2


discriminant = b*b - 4*a*c
discriminant = sqrt(discriminant)

xplus  = (-b + discriminant) / (2*a)
xminus = (-b - discriminant) / (2*a)

print ('The roots of ax **2 + bx + c = 0 with',
       'a =', a, ' b =', b ,' c =', c, 'are', xminus , xplus)

