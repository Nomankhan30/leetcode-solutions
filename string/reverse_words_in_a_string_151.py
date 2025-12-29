class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        string = ""

        #Normalize string and eliminate extra spaces
        for i in range(len(s)):
            if s[i] != " ":
                string += s[i]
            else:
                if string != "":
                    words.append(string)
                    string = ""

        # add last word if exists
        if string != "":
            words.append(string)

        # build reversed sentence
        revSentence = ""
        for i in range(len(words) - 1, -1, -1):
            revSentence += words[i]
            if i != 0:
                revSentence += " "

        return revSentence
