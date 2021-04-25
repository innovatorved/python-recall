class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        val = [[],[],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]

        in_ele = []
        #print(digits)
        for x in digits:
            in_ele.append(val[int(x)])
        # print(in_ele)
        n = len(in_ele)

        if n == 1:
            return in_ele[0]

        elif n == 0:
            return in_ele

        elif n >= 2:
            ans = []
            for i in in_ele[0]:
                for j in in_ele[1]:
                    ans.append(f"{i}{j}")
            if n >= 3:
                res = []
                for i in ans:
                    for j in in_ele[2]:
                        res.append(f"{i}{j}")
                if n == 4:
                    ser = []
                    for i in res:
                        for j in in_ele[3]:
                            ser.append(f"{i}{j}")
                    return ser
                else :
                    return res
            else:
                return ans
