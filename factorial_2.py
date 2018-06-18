def factorial (n):
    fact = 1
    if not isinstance(n, int) or n < 0:
        raise ValueError ('wtf')
    for i in range (n, 1, -1):
        return n*factorial(n-1)
##        n = n-1
        print(i)
    return n
#print(factorial(6))

def test_factorial():
    takes = [ 0, -5]
    gives = [ 1, ValueError]
    for i in range (len(takes)):
        assert (factorial(takes[i]) == gives[i])
        print("good to go")
test_factorial()
