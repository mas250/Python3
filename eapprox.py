def eapprox(number):
    factorial = 1
    total = 1
    for i in range (1, number+1):
        
        factorial = factorial * i
        total = 1 / factorial + total
    print(total)

number = int(input("enter  number" ))

eapprox(number)
