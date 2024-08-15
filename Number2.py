def solution(A):
    i = 0
    length = len(A) 
    
    ways = 0
    for i in range(1, length):
        first_half = A[:i]
        second_half = A[i:]
        if first_half.count('x') == first_half.count('y') or second_half.count('x') == second_half.count('y'):
            ways += 1

    return ways 

print(solution('ayxbx'))
print(solution('xzzzy'))
print(solution('toyxmy'))
print(solution('apple'))