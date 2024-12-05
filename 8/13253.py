from itertools import product
k=0
m=0

for i in product("КОНЕЦ",repeat=5):
    w1="".join(i)
    if 'Е' in w1 or 'Ц' in w1:
        k+=1
for j in product ("ДРАКОН",repeat=5):
    w2="".join(j)
    if 'Д' in w2 or 'Р' in w2 or 'А' in w2:
        m+=1
print(m+k)