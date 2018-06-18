def fracsum(number):
    fracsum = 1
    total = 0
    for i in range (0, number):
        
        fracsum = 1/ number**i
        total = fracsum + total
    print(total)

number = int(input("enter  number" ))
fracsum(number)
