def GreedyCoins(M,k):
    n=len(M)
    l=[]
    flag=False
    x=0
    while (flag != True and  x!=(n)):
        if M[x]<=k:
            num = k // M[x]
            k=k%M[x]
            for y in range (0,num):
                l.append(M[x])
        if k==0:
            flag=True
        x += 1

    for x in l:
        print(x)


GreedyCoins([100,50,10],70)




