def reverse_list(user_list):
    for i in user_list:
        backwards_list.insert(0, i)
    print (backwards_list)
user_list = ['red', 'yellow' , 'green']
backwards_list = []

reverse_list(user_list)

