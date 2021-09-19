class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        k = 1

        def swap(x,y):
            nums[x], nums[y] = nums[y], nums[x]

        for i in range(2, len(nums)):
            if nums[i]!=nums[k] or nums[i]!=nums[k-1]:
                swap(k+1, i)
                k += 1

        return k+1
