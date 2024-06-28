def recursive_binary_search(lst,target):
    if len(lst) == 0:
        return False
    
    else:
        midpoint = len(lst)//2
        if lst[midpoint] == target:
            return midpoint
        
        else:
            if lst[midpoint] < target:
                return recursive_binary_search(lst[midpoint+1:],target)

            else:
                return recursive_binary_search(lst[:midpoint],target)


newLst = [1,6,3,9,10]
newLst.sort()
targ = 6
print(recursive_binary_search(newLst,targ))