class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = 0

        target = {}
        for ch in t:
            target[ch] = target.get(ch, 0) + 1

        window = {}
        required = len(target)
        formed = 0

        min_len = float('inf')
        min_start = 0
        

        for r in range(len(s)):

            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in target and window[s[r]] == target[s[r]]:
                formed += 1
                
            while formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_start = l

                window[s[l]] -= 1

                if s[l] in target and window[s[l]] < target[s[l]]:
                    formed -= 1

                l += 1


        if min_len == float('inf'):
            return ""

        return s[min_start: min_start + min_len]




        