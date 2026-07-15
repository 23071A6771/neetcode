class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=float("-inf")
        for i in range(len(nums)):
            if nums[i]>=maj:
                maj=max(maj,nums[i])
        return maj
        