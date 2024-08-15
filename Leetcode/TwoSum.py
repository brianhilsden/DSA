"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""


def twoSum(nums,target):
    dicti = {}
    leng = len(nums)

    for i in range(leng):
        complement = target - nums[i]
        if complement in dicti:
            return [dicti[complement],i]
        dicti[nums[i]] = i

    return []