class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = list(zip(*strs))
        P = ""
        for i in l:
            if len(set(i))==1:
                P += i[0]
            else:
                break
        return P
