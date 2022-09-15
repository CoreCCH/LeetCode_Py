class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i,a in enumerate(strs[0]):
            for j,b in enumerate(strs):
                if i < len(strs[j]):
                    if a == strs[j][i]:
                        pass
                    else:
                        return res
                else:
                    return res
            res = res+a
        return res