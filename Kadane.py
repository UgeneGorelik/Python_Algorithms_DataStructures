def solution(A):
    max_sum=0
    cur_sum=0
    for x in range(0,len(A)-1):
        cur_sum=max(cur_sum+A[x],cur_sum)
        max_sum=max(max_sum,cur_sum)
    print(max_sum)


solution([-2,3,2,-1])

