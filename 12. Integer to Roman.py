class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        cnt = int(num / 1000)
        for i in range(cnt):
            result = result+'M'
        num = int(num % 1000)
        cnt = int(num / 100)
        if cnt <= 3:
            for i in range(cnt):
                result = result + 'C'
        elif cnt > 3 and cnt <= 5:
            for i in range(5 - cnt):
                result = result + 'C'
            result = result + 'D'
        elif cnt > 5 and cnt < 9:
            result = result + 'D'
            for i in range(cnt-5):
                result = result + 'C'
        elif cnt >= 9:  
            for i in range(10 - cnt):
                result = result + 'C'
            result = result + 'M'    
        num = int(num % 100)
        cnt = int(num / 10)
        if cnt <= 3:
            for i in range(cnt):
                result = result + 'X'
        elif cnt > 3 and cnt <= 5:
            for i in range(5 - cnt):
                result = result + 'X'
            result = result + 'L'
        elif cnt > 5 and cnt < 9:
            result = result + 'L'
            for i in range(cnt-5):
                result = result + 'X'
        elif cnt >= 9:  
            for i in range(10 - cnt):
                result = result + 'X'
            result = result + 'C'    
        num = int(num % 10)
        cnt = num
        if cnt <= 3:
            for i in range(cnt):
                result = result + 'I'
        elif cnt > 3 and cnt <= 5:
            for i in range(5 - cnt):
                result = result + 'I'
            result = result + 'V'
        elif cnt > 5 and cnt < 9:
            result = result + 'V'
            for i in range(cnt-5):
                result = result + 'I'
        elif cnt >= 9:  
            for i in range(10 - cnt):
                result = result + 'I'
            result = result + 'X'  
        return result
            