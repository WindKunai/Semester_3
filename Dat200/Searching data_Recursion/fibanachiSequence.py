def fib(n):
    first,second=0,1
    for i in range(n):
        temp = first
        first = second
        second = second + temp
    return first

print(fib(12))


### With recersive n^th

def fibonacci(n):
    if n in {0, 1}: # Base case
        return n
    return fibonacci(n-2)+fibonacci(n -1)
