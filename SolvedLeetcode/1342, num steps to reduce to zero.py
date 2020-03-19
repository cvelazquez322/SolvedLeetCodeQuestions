# Given a non-negative integer num, 
# return the number of steps to reduce it to zero.
 # If the current number is even, you have to divide it by 2,
 # otherwise, you have to subtract 1 from it.

def nosHelper(num, step):
    if num == 0:
        return step
    step += 1
    if num % 2 == 0:
        num /= 2
        return nosHelper(num, step)
    else:
        num -= 1
        return nosHelper(num, step)
    
    

class Solution:
    def numberOfSteps (self, num: int) -> int:
        return nosHelper(num, 0)
        