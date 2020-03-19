# Given an array nums of integers, 
# return how many of them contain an even number of digits.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0
        for item in nums:
            tmp = str(item)
            if len(tmp) % 2 == 0:
                counter += 1
        return counter