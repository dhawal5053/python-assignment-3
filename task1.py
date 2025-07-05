def factorial(n):
    if n<2:
        return 1
    else:
        return n * (factorial(n-1))

a=5
result = factorial(a)

print('Factorial of '+str(a)+' is:',result)