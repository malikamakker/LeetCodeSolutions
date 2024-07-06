class Solution:
    def find_max_index_in_array(self, array, start, end, value):
        while start <= end:
            mid = int((start + end) / 2)
            mid_value = array[mid]
            if mid_value <= value:
                start = mid + 1
            elif mid_value > value:
                end = mid - 1
        return start
    
    def find_min_index_in_array(self, array, start, end, value):
        while start <= end:
            mid = int((start + end) / 2)
            mid_value = array[mid]
            if mid_value < value:
                start = mid + 1
            elif mid_value >= value:
                end = mid - 1
        return start

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        is_even = (len(nums1) + len(nums2)) % 2 == 0
        median_idx = int((len(nums1) + len(nums2)) / 2)
        indices_to_compute = []
        median_values = {}

        if is_even:
            indices_to_compute = [median_idx - 1, median_idx]
        else:
            indices_to_compute = [median_idx]

        
        def find(lookup_array, search_array):
            for index in indices_to_compute:                
                lookup_start = 0
                lookup_end = len(lookup_array) - 1

                search_start = 0
                search_end = len(search_array) - 1

                while lookup_start <= lookup_end:
                    lookup_mid = int((lookup_start + lookup_end) / 2)
                    value = lookup_array[lookup_mid]
                    max_search_index = self.find_max_index_in_array(search_array, search_start, search_end, value)
                    min_search_index = self.find_min_index_in_array(search_array, search_start, search_end, value)
                    max_computed_index = max_search_index + lookup_mid
                    min_computed_index = min_search_index + lookup_mid
                    if index >= min_computed_index and index <= max_computed_index:
                        median_values.update({index: value})
                        break
                    elif min_computed_index > index:
                        lookup_end = lookup_mid - 1
                        search_end = min_search_index if min_search_index < search_end else search_end
                    else:
                        lookup_start = lookup_mid + 1
                        search_start = max_search_index if search_start < max_search_index else search_start

        lookup_array = nums1
        search_array = nums2

        find(lookup_array, search_array)

        if len(median_values) != len(indices_to_compute):
            lookup_array = nums2
            search_array = nums1
            find(lookup_array, search_array)
        
        median_values = list(median_values.values())
        return median_values[0] if not is_even else (median_values[0] + median_values[1])/2
        