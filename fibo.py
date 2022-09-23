import math


n = int(input())

def binets_formula(n):

    """
    The central function implementing Binet's Formula
    """

    # pre-calculate sqrt(5) as we use it 3 times
    sqrt5 = math.sqrt(5)

    F_n = int((( (1 + sqrt5) ** n - (1 - sqrt5) ** n ) / ( 2 ** n * sqrt5 )))

    return F_n

print(binets_formula(n))
