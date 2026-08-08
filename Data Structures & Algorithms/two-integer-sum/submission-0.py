class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range (len(nums)):
            for j in range ((i+1), len(nums)):
                if (nums[i] + nums[j]) == target:
                    if i<j :
                        arr = [i, j]
                    else:
                        arr = [j, i]
        return arr