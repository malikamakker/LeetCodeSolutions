import java.util.*;
class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> hash = new HashMap<Character, Integer>();
        int len = 0;
        int maxLen = 0;
        
        for (int i=0; i < s.length(); i++) {
            if (hash.get(s.charAt(i)) == null || hash.get(s.charAt(i)) == -1) {
                hash.put(s.charAt(i), i);
                len++;
            } else {
                int match = hash.get(s.charAt(i));
                for(Map.Entry<Character, Integer> entry: hash.entrySet()) {
                    if (entry.getValue() < match) {
                        hash.put(entry.getKey(), -1);
                    }
                }
                hash.put(s.charAt(i), i);
                maxLen = Math.max(len, maxLen);
                len = i - match;
            }
        }
        maxLen = Math.max(len, maxLen);
        return maxLen;
    }
}
