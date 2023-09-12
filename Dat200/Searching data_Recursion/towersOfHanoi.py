def moveTower(n, source, dest, temp):
    if n == 1:
        print "Move disk from", source, "to", dest+".“
    else:
        moveTower(n-1, source, temp, dest)
        moveTower(1, source, dest, temp)
        moveTower(n-1, temp, dest, source)

### Or 

def hanoi(n,a,b,c):
    if n ==1:
        print("move disk", n, "from", a , "to", c)
    else:
        hanoi(n-1, a,c,b)
        print("move disk", n, "from", a , "to", c)
        hanoi(n-1, b, a,c)
        hanoi(3,'a','b','c')

