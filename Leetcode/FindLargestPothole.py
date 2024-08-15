def solution(R, N):
    max_product = 0
    current_largest = 0
    current_length = 0
    
    for i in range(N):
        if R[i] != 0:
            current_length += 1
            if R[i] > current_largest:
                current_largest = R[i]
        else:
            if current_length > 0:
                product = current_largest * current_length
                if product > max_product:
                    max_product = product
                current_largest = 0
                current_length = 0
    
   
    if current_length > 0:
        product = current_largest * current_length
        if product > max_product:
            max_product = product
    
    return max_product


print(solution([9, 8, 7, 0, 0, 0, 2,3,9,4], 10)) 
