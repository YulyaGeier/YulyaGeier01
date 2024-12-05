from itertools import product
a=product('ЛЮСТРА', repeat=5)
k=0

for i in a:
    word="".join(i)
    if word.count("Ю")<3 and word[-1] not in 'ЛСТР':
                k+=1
print(k)