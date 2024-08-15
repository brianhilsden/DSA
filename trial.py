def mySqrt(x):
    if x<2:
        return x

    first = 2
    last = x//2

    while first <= last:
        midpoint = (first+last)//2
        square = midpoint * midpoint
        if square == x:
            return midpoint
        elif x >square:
            first = midpoint+1

        else:
            last = midpoint-1
    return last

print(mySqrt(9))