def binary_search(lst,target):
    first = 0
    last = len(lst)-1

    while first<=last:
        midpoint = (first+last)//2

        if lst[midpoint] == target:
            return midpoint
        
        elif lst[midpoint] < target:
            first = midpoint + 1
        
        else:
            last = midpoint -1

    return False



newLst = [1,6,3,9,10]
newLst.sort()
targ = 6


print(binary_search(newLst,targ))