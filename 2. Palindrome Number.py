class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        R = 0
        O = x
        while x > R:
            R = R * 10 + x % 10
            x //= 10
        return x == R or x == R // 10
