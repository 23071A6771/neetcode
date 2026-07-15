class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap={}
        for i,n in enumerate(nums):
            r = target - nums[i]
            if r in hmap:
                return [hmap[r],i]
            hmap[n]=i
        