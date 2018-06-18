fib_list = [0, 1]
fib_value = 0
def fib (user_number):
    for i in range (user_number - 2):
        fib_value = fib_list[-1] + fib_list[-2]
        fib_list.append(fib_value)
        prev = fib_value
    return fib_value

    
user_number = int(input('Enter a number: '))
fib(user_number)
for i in fib_list:
    print (i)
