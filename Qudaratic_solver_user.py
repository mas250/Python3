#quadratic solver

from math import sqrt

a = int(input('Enter a value for a: '))
b = int(input('Enter a value for b: '))
c = int(input('Enter a value for c: '))


discriminant = b*b - 4*a*c
discriminant = sqrt(discriminant)

xplus  = (-b + discriminant) / (2*a)
xminus = (-b - discriminant) / (2*a)

print ('The roots of ax **2 + bx + c = 0 with',
       'a =', a, ' b =', b ,' c =', c, 'are\n\n', xminus , xplus)

