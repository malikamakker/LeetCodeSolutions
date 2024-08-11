class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_lower_count = [0 for _ in range(26)]
        char_upper_count = [0 for _ in range(26)]
        for c in t:
            if c.isupper():
                char_upper_count[ord(c)-65] += 1
            else:
                char_lower_count[ord(c)-97] += 1
        current_lower_count = [0 for _ in range(26)]
        current_upper_count = [0 for _ in range(26)]
        window = float('inf')
        start=-1
        end=-1

        last_index_lower = [[] for _ in range(26)]
        last_index_upper = [[] for _ in range(26)]
        idx = 0

        for c in s:
            if c.isupper():
                actual_count = char_upper_count[ord(c)-65]
                current_upper_count[ord(c)-65] += 1
                last_index_upper[ord(c)-65].append(idx)
            else:
                actual_count = char_lower_count[ord(c)-97]
                current_lower_count[ord(c)-97] += 1
                last_index_lower[ord(c)-97].append(idx)

            lower_valid = [False for _ in range(26)]
            upper_valid = [False for _ in range(26)]
            indices = []
            for i in range(26):
                actual_upper = char_upper_count[i]
                actual_lower = char_lower_count[i]
                current_upper = current_upper_count[i]
                current_lower = current_lower_count[i]
                if actual_upper and current_upper // actual_upper >= 1:
                    upper_valid[i] = True
                    indices.append(last_index_upper[i][-actual_upper])
                if not actual_upper:
                    upper_valid[i] = True
                if actual_lower and current_lower // actual_lower >= 1:
                    lower_valid[i] = True
                    indices.append(last_index_lower[i][-actual_lower])
                if not actual_lower:
                    lower_valid[i] = True
            if all(upper_valid) and all(lower_valid):
                max_idx = min(indices) if indices else None
                if max_idx!=None and (idx - max_idx + 1) < window:
                    window = idx - max_idx + 1
                    start = max_idx
                    end = idx
            idx += 1
        return s[start:end+1]
        