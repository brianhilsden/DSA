def binary_search(nums,target):
    if len(nums) == 0:
        return 0
    first = 0
    last = len(nums)-1
    while first<=last:
        midpoint = (first+last)//2
        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] < target:
            first = midpoint + 1
        
        else:
            last = midpoint -1

    if nums[midpoint] < target:

        return midpoint+1
    else:
        return midpoint


lst = [1,3,5,6,21,28,89,91,100,130,150]

print(binary_search(lst,7))


