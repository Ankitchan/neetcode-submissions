class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left, right = 0, 0

        setCh = set()
        max_len = 0
        while(right < len(s)):
            if s[right] not in setCh:
                setCh.add(s[right])
                right += 1
                max_len = max(max_len, right - left)
            else:
                setCh.remove(s[left])
                left += 1
            
        return max_len

