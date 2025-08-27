class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = []
        length = []
        for i in range(len(s)):
            for j in range(i,len(s)):
                string = s[i:j+1]
                if string == string[::-1]:
                    l.append(string)
                    length.append(len(string))
        maxi_index = length.index(max(length))
        return l[maxi_index]
