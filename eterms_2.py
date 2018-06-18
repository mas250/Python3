def eterms(tol=0.001):
    """
    Find the number of terms needed to approximate e to the given tolerance
    """
    from math import e

    terms = 1
    approx = 1
    fact = 1
    while abs(approx - e) > tol:
        fact = fact * terms      # Factorial of the number of terms
        approx = approx + 1/fact
        terms = terms + 1
    return terms

# Try it
tolerance = 0.0001
terms = eterms(tolerance)
print(terms, "terms needed for a tolerance of", tolerance)
