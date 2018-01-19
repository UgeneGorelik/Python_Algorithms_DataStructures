def solution(A):
 max_ending = max_slice = 0
 for a in A:
    max_ending = max(0, max_ending + a)
    max_slice = max(max_slice, max_ending)
 return max_slice


solution([-2,3,2,-1])

