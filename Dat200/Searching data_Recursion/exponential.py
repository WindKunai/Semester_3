def exp1(x, n):
    base = x
    exponent = n
    result = 1
    for exponent in range(exponent, 0, -1):
        result *= base
    return result

print(exp1(2,3))


### Or 

def exp2(x, n):
    if n == 0:
        return 1
    else:
        return x * exp2(x, n-1)
    
print(exp2(2,3))