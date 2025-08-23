from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        common_prefix = ""
        mini = min(len(s) for s in strs)

        for i in range(mini):
            ch = strs[0][i]
            
            if all(s[i] == ch for s in strs):
                common_prefix += ch
            else:
                break  
        
        return common_prefix
