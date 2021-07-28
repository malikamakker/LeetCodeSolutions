class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        def trace(nums, index, last_index, visited):
            if index == last_index:
                return False
            if visited[index]:
                if nums[index] < 0:
                    return retrace(nums, index, -1, False, True)
                else:
                    return retrace(nums, index, -1, True, False)

            next_index = (index + nums[index]) % len(nums)
            if next_index < 0:
                next_index = len(nums) - next_index
            visited[index] = True

            return trace(nums, next_index, index, visited)

        def retrace(nums, initial, current, pos, neg):
            if current == initial:
                return True
            if current > 0:
                if pos:
                    if nums[current] < 0:
                        return False
                if neg:
                    if nums[current] > 0:
                        return False
            else:
                current = initial

            next_index = (current + nums[current]) % len(nums)
            if next_index < 0:
                next_index = len(nums) - next_index

            return retrace(nums, initial, next_index, pos, neg)

        start = 0
        while start < len(nums):
            visited = [False for i in range(len(nums))]
            loop = trace(nums, start, -1, visited)
            if loop:
                return True
            while start < len(visited) and visited[start]:
                start = start + 1
        return False
