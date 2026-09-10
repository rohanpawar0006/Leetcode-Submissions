class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSub = nums[0]
        
        for i in range(1, len(nums)):
            j = nums[i]
            currSum = max(j, currSum + j)
            maxSub = max(currSum, maxSub)
            
        return maxSub