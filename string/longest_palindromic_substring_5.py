class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        lastpal = ""

        # helper: expand around center
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # return palindrome found
            return s[left + 1:right]

        for i in range(len(s)):
            # Odd length palindrome (center at i)
            lpal1 = expand(i, i)
            # Even length palindrome (center between i and i+1)
            lpal2 = expand(i, i + 1)

            # Choose the longer one
            lpal = lpal1 if len(lpal1) > len(lpal2) else lpal2

            # Update lastpal if needed
            if len(lpal) > len(lastpal):
                lastpal = lpal

        return lastpal
