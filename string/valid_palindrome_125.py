class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True  # empty string is a palindrome
        
        # filter only letters and convert to lowercase
        newpal = ""
        for ch in s:
            ch = ch.lower()
            #ignore element if element not in alphabet or numeric.
            if ch.isalnum():
                newpal += ch

        # two pointers
        left = 0
        right = len(newpal) - 1

        while left < right:
            if newpal[left] == newpal[right]:
                left += 1
                right -= 1
            else:
                return False

        return True

sol = Solution()

print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(sol.isPalindrome("race a car"))                       # False
print(sol.isPalindrome(" "))                                # True
print(sol.isPalindrome("0P"))