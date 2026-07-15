class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(0,n):
            r = target - nums[i]
            j=nums.index(r)
            if r in nums and j!=i:
                return [min(j,i),max(j,i)]
        return [-1,-1]
        