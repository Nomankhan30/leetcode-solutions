class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Edge case: if t is longer than s, impossible
        if len(t) > len(s):
            return ""

        left = 0

        needFreq = {}     # frequency of characters needed
        window = {}       # frequency of characters in current window

        windowSize = float("inf")
        res = [-1, -1]

        reqcount = 0      # how many unique characters are satisfied

        # Build need frequency dictionary
        for c in t:
            needFreq[c] = needFreq.get(c, 0) + 1

        needCount = len(needFreq)  # number of unique required characters

        # Expand window
        for right in range(len(s)):
            ch = s[right]

            window[ch] = window.get(ch, 0) + 1

            # If requirement just satisfied
            if ch in needFreq and window[ch] == needFreq[ch]:
                reqcount += 1

            # Shrink window when valid
            while reqcount == needCount:

                # Update minimum window
                if (right - left + 1) < windowSize:
                    windowSize = right - left + 1
                    res = [left, right]

                leftChar = s[left]
                window[leftChar] -= 1

                # If a required character becomes insufficient
                if leftChar in needFreq and window[leftChar] < needFreq[leftChar]:
                    reqcount -= 1

                left += 1

        # If no valid window found
        if res[0] == -1:
            return ""

        return s[res[0]:res[1] + 1]
