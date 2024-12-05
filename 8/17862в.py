from itertools import product
k=0

for i in product("0123456789AB", repeat=5):
    word="".join(i)
    if word[0]!=0 and word.count('7')==1 and word.count("9")+word.count("A")+word.count("B")<=3:
        k+=1
print(k)