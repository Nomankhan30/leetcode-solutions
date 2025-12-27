from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for word in strs:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1

            key = tuple(freq)
            if key in dic:
                dic[key].append(word)
            else:
                dic[key] = [word]

        return list(dic.values())
