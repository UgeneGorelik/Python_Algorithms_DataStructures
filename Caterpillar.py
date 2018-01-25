def caterpillar(A,s):
    front=0
    total=0
    n=len(A)
    for back in range(n):
        while (front < n and total + A[front] <= s):
            total=total+A[front]
            front+=1
        if total==s:
            return True
        else:
            total-=A[back]

print(caterpillar([6,2,7,4,1,3,6],12))