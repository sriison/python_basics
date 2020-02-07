def factoria(n):
    if (n ==1 or n == 0):
        return 1;
    else:
        return n * factoria(n-1);
#alternate sol
# n=5
# print (factorial(n))
print (factoria(5))