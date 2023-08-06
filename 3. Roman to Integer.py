class Solution:
    def romanToInt(self, s: str) -> int:
        Num = ["I", "V", "X", "L", "C", "D", "M"]
        N1 = [1, 5, 10, 50, 100, 500, 1000]
        T = 0
        for char in s:
            for i in range(len(Num)):
                if char == Num[i]:
                    T += N1[i]
        if "IV" in s or "IX" in s:
            T -= 2
        if "XL" in s or "XC" in s:
            T -= 20
        if "CD" in s or "CM" in s:
            T -= 200
        return T
