def longestValidParentheses(s:str):
    ans = 0
    str_list = []
    for i in s:
        str_list.append(i)
    buffer = []
    while(str_list != []):
        x = str_list.pop()
        if buffer == []:
            if x == ")":
                buffer.append(x)
        elif x == "(" and buffer[-1] == ")":
            ans = ans + 2
            buffer.pop()
        elif x == ")":
            buffer.append(x)
        
    print(ans)        

longestValidParentheses("()(())")