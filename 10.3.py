import string
import re
fname=open('letter.txt')
d=dict()
for line in fname:
    line=line.rstrip()
    line=line.lower()
    al=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
        for n in line:
        if n in al:
            d[n]=d.get(n,0)+1
count=0
for k in d:
    count+=d[k]

    
p=list()
for k in d:
    p.append((round((d[k]/count*100),1),k))

p.sort(reverse=True)
for n,m in p:
    print(m,' :',n)
