class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        for i in range(len(s)):
            if s[i] == 'M':
                result = result+sym[s[i]]
            elif s[i] == 'C':
                if i<len(s)-1:
                    if s[i+1] == 'D' or s[i+1] == 'M':
                        result = result-sym[s[i]]
                    else:
                        result = result+sym[s[i]]
                else:
                    result = result+sym[s[i]]
            elif s[i] == 'D':
                result = result+sym[s[i]]
            elif s[i] == 'X':
                if i<len(s)-1:
                    if s[i+1] == 'C' or s[i+1] == 'L':
                        result = result-sym[s[i]]
                    else:
                        result = result+sym[s[i]]
                else:
                    result = result+sym[s[i]]
            elif s[i] == 'L':
                result = result+sym[s[i]]
            elif s[i] == 'I':
                if i<len(s)-1:
                    if s[i+1] == 'X' or s[i+1] == 'V':
                        result = result-sym[s[i]]
                    else:
                        result = result+sym[s[i]]
                else:
                    result = result+sym[s[i]]
            elif s[i] == 'V':
                result = result+sym[s[i]]

        return result