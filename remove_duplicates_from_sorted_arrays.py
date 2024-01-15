'''
'''
def removeDuplicates(nums):
    i = 0
    j = 1
    if len(nums) == 1:
        return len(nums)
    elif len(nums) == 2:
        if nums[0] == nums[1]:
            nums.remove(nums[1])
            return 1
        else:
            return len(nums)
    else:
        while i < len(nums) and j < (len(nums)):
            if nums[i] == nums[j]:
                nums.remove(nums[j])
                j = i + 1
                #i += 1
            else:
                i += 1
                j += 1
        return (print(nums))


nums = [0,1,1,1,2,2,3,3,4] 
#nums = [1,2,2]
#nums = [1,1,1]       
removeDuplicates(nums)


'''
Example 1:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 2, nums = [0,1,2,3,4]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''