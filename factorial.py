def factorial(number):
    factorial = 1
    for i in range (1, number+1):
        
        factorial = factorial * i
    print(factorial)

number = int(input("enter  number" ))
factorial(number)
print(factorial)
