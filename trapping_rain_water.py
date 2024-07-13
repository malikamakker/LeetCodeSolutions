class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_array = []
        max_left = 0
        for h in height:
            if h > max_left:
                max_left = h
            max_left_array.append(max_left)
        
        max_right = 0
        storage = 0
        left_index = len(height) - 1

        for h in reversed(height):
            if h > max_right:
                max_right = h
            max_left = max_left_array[left_index]
            if h < max_left and h < max_right:
                total_depth = min(max_left, max_right)
                storage += total_depth - h
            left_index -= 1

        return storage
        