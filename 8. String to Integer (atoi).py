class Solution:
    def myAtoi(self, s: str) -> int:
        if (len(s) > 1):
            for i in range(len(s)-1):
                ans = 0
                if (ord(s[i])<=90 and ord(s[i])>=65) or (ord(s[i])<=122 and ord(s[i])>=97) or ord(s[i]) == 46:
                    return(ans)
                else:
                    if s[i] == '-':
                        if ord(s[i+1])> 47 and ord(s[i+1]) < 58:
                            i = i + 1
                            ans = ans*10+int(s[i])
                            i = i + 1
                            while(1):
                                if i<len(s):
                                    if (ord(s[i])> 47 and ord(s[i]) < 58):
                                        ans = ans*10+int(s[i])
                                        i = i + 1

                                    else:
                                        if ans*-1 < -2**31:
                                            return(-2**31)
                                        else:
                                            return(ans*-1)
                                else:
                                    if ans*-1 < -2**31:
                                        return(-2**31)
                                    else:
                                        return(ans*-1)
                        else:
                            return(0)

                    if s[i] == '+':
                        if ord(s[i+1])> 47 and ord(s[i+1]) < 58:
                            i = i + 1
                            ans = ans*10+int(s[i])
                            i = i + 1
                            while(1):
                                if i<len(s):
                                    if (ord(s[i])> 47 and ord(s[i]) < 58):
                                        ans = ans*10+int(s[i])
                                        i = i + 1

                                    else:
                                        if ans > 2**31-1:
                                            return(2**31-1)
                                        else:
                                            return(ans)
                                else:
                                    if ans > 2**31-1:
                                        return(2**31-1)
                                    else:
                                        return(ans)
                        else:
                            return(0)

                    if ord(s[i])> 47 and ord(s[i]) < 58:    
                        ans = ans*10+int(s[i])    
                        i = i + 1
                        while(1):
                            if i<len(s):
                                if (ord(s[i])> 47 and ord(s[i]) < 58):
                                    ans = ans*10+int(s[i])
                                    i = i + 1
                                else:
                                    if ans > 2**31-1:
                                        return(2**31-1)
                                    else:
                                        return(ans)
                            else:
                                if ans > 2**31-1:
                                    return(2**31-1)
                                else:
                                    return(ans)
            return ans
        elif (len(s) == 1):
            if (ord(s)<=90 and ord(s)>=65) or (ord(s)<=122 and ord(s)>=97) or ord(s) == 46 or ord(s) == 43 or ord(s) == 45 or s == " ":
                return(0)
            else:
                return(int(s))
        else:
            return(0)
