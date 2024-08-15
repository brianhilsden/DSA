def removeDuplicates(nums):
    k = 1
    if not nums:
        return 0

    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[ k] = nums[i]
            k+=1
    print(nums)
    return k
  
lst = [1,1,2,3,4,4,5,6]

print(removeDuplicates(lst))