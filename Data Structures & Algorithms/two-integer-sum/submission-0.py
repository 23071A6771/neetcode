class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(0,n):
            r = target - nums[i]
            if r in nums:
                return [min(nums.index(r),i),max(nums.index(r),i)]
        return [-1,-1]
        