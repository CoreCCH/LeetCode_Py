class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s    

        get_res = []
        for i in range(numRows):
            get_res.append('')
        x = 0
        way = True
        for i,a in enumerate(s):
            if x == numRows - 1:
                way = False
            elif x == 0:
                way = True    
            get_res[x] = get_res[x]+a

            if way == True:
                x += 1
            else:
                x -= 1
        res = ''
        for a in get_res:
            res = res+a

        return res   