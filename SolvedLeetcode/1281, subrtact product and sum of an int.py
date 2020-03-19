# Given an integer number n, 
# return the difference between the product of its digits 
# and the sum of its digits.


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nl = list(str(n))
        sumo = 0
        prod = 1
        for x in nl:
            sumo += int(x)
            prod *= int(x)
        return prod - sumo