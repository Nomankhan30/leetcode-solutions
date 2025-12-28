class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0  # by definition, empty needle occurs at index 0

        hlen = len(haystack)
        nlen = len(needle)

        for i in range(hlen - nlen + 1):
            j = 0
            while j < nlen and haystack[i + j] == needle[j]:
                j += 1

            if j == nlen:
                return i  # first occurrence index

        return -1
