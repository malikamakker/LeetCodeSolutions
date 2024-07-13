class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        for num in range(2**len(nums)):
            subset = []
            for bit in range(len(nums)):
                is_set = num & 1
                num=num>>1
                if is_set:
                    subset.append(nums[bit])
            subsets.append(subset)
        return subsets
        