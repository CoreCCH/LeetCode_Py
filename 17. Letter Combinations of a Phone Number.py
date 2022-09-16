class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno', '7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        res_por = []
        for i,a in enumerate(digits):
            if i == 0:
                for j in mapping[a]:
                    res_por.append(j)

                res = res_por.copy()
                res_por.clear()

            else:
                for j in res:
                    for k in mapping[a]:
                        res_por.append(j+k)
                res = res_por.copy()
                res_por.clear()

        return res