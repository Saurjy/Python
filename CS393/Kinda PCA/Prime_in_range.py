import sympy
A = int(input("ENTER THE LOWER RANGE : "))
B = int(input("ENTER THE HIGHER RANGE : "))
print (list(sympy.sieve.primerange(A, B)))
