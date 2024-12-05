from itertools import product
k=0

for i in product("0123456",repeat=7):
    w="".join(i)
    if w[0]!=0 and w.count("0")+w.count("2")+w.count("4")+w.count("6")==2:
        k+=1
print(k)