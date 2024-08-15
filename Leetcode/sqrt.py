def squareRoot(num):
    if num<2:
        return num
    
    first,last = 2, num//2

    while first<=last:
        mid = (first+last)//2
        mid_squared = mid * mid

        if mid_squared == num:
            return mid
        
        elif mid_squared < num:
            first = mid +1

        else:
            last = mid - 1


    return last

print(squareRoot(8))