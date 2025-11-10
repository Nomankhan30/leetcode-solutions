class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        hashtab = {}
        result = ""
        max_sub = ""

        for i in range(len(s)):
            ch = s[i]

            # If character already seen and inside window
            if ch in hashtab and hashtab[ch] >= start:
                start = hashtab[ch] + 1  # move window

            hashtab[ch] = i  # store latest index
            window = s[start:i + 1]  # current substring window
            # print("Window:", window)  # can uncomment for debugging

            if len(window) > len(max_sub):
                max_sub = window

        return len(max_sub)
