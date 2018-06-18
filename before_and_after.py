def before_and_after(foods, before, after):
    for i in foods:
        food_list.append(i)
        print(before, i , after)
    

foods  = ['ham', 'toast', 'spam', 'bacon', 'spinach']
before = 'Would you like '
after  = 'and eggs?'
food_list = []
before_and_after(foods, before, after)
#print(before, food_list, after)
