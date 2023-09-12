mylist = [1,2,3,4,5,6,7,8]

k = 3
print(mylist)
for i in range(1, k):
    mylist[i-1] = mylist[-i]
    mylist[-i] = mylist[i-1]
print(mylist)