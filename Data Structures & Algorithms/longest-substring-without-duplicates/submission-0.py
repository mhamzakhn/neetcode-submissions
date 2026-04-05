class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        longest = 0
        counter = {}

        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1

            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1

            longest = max(longest, r - l + 1)

        return longest
            


        