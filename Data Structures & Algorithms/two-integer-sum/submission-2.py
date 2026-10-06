class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for i, val in enumerate(nums):
            need = target - val
            if need in check:
                return [check[need], i]
            check[val] = i