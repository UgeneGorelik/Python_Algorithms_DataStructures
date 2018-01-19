def MooresDominator(A):
    candidate = 0
    count = 0
    for x in range(0, len(A) - 1):
        if count == 0:
            candidate = A[x]
            count += 1
        else:
            if A[x] != candidate:
                count -= 1
            else:
                count += 1

    count = 0
    for x in A:
        if x == candidate:
            count += 1
    if count >= (len(A) // 2):
        print(candidate)


MooresDominator([3, 2, 3, 4, 3, 3, 3, -1])