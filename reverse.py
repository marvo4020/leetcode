class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_x = int(str(x_abs)[::-1])
        result = sign * reversed_x
        return result if -2**31 <= result <= 2**31 - 1 else 0
