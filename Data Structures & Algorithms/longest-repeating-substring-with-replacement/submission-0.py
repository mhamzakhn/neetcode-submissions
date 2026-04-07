class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        hashmap = {}
        longest = 0
        maxf = 0

        for r in range(0, len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            maxf = max(maxf, hashmap[s[r]])

            while (r - l + 1) - maxf > k:
                hashmap[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest

            

        