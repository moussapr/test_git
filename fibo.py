import random
liste=[]
nb0=0
nb1=1
liste.append(nb0)
liste.append(nb1)
for i in range (0,15):
    
        nb=nb0+nb1
        nb0=nb1
        nb1=nb
        liste.append(nb)

print (liste)

#fonction avec récursivité

def fibo (n,un=1,un1=1):
        print(un)
        return fibo(n-1,un1,un1+un) if n else un

fibo(15)