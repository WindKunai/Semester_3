import random as rdm

rc = [rdm.randint(0, 100) for i in range(20)]
print("The original list", rc)

i = 0
while i < len(rc) - 1:
    if rc[i] > rc[i + 1]:
        rc.pop(i + 1)
    else:
        i += 1

print("The modified list", rc)
