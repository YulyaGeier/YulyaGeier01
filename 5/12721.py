p=[]
for n in range (1,1000):
    b=oct(n)[2:]
    if (b.count('0')+b.count('2')+b.count('4')+b.count('6')+b.count('8'))%2==0:
        b=(oct((n%8)*5)[2:])+b
    else:
        b=b[-3:] +'46'
    r=int(b,8)
    if n>= 80:
        p.append(r)
print(min(p))