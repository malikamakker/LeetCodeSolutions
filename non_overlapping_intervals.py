class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        cache = {}
        i = intervals[0][0]
        max_intervals = 0
        interval = intervals[0]
        last_count = 0
        intervals_index = 0

        while i <= intervals[-1][1]:
            start = interval[0]
            cache.setdefault(i, 0)
            if i == interval[1]:
                cache[i] = max(max_intervals, cache.get(start, 0) + 1)
                intervals_index += 1
                max_intervals = max(cache.get(i), max_intervals)
                if intervals_index >= len(intervals):
                    break
                interval = intervals[intervals_index]
            else:
                cache[i] = max_intervals
            
            if i == interval[1]:
                continue
            i += 1
        return len(intervals) - max_intervals
        