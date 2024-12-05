from itertools import product
k=0

for i in product('01234567',repeat=5):
    w="".join(i)
    if w[0] not in '01357' and w[-1] not in '26' and w.count('7')<3:
        k+=1
print(k)