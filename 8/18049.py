from itertools import product
a=product('012345678',repeat=7)
k = 0

for i in a:
    word="".join(i)
    if word[0] not in '0246':
        if word[-1]!=word[-2] or word[-2]!=word[-3] or word[-1]!=word[-3]:
            k += 1
print (k)