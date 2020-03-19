# # Given the array nums, for each nums[i] find out how many 
# numbers in the array are smaller than it. 
# That is, for each nums[i] you have to count the number of valid j's 
# such that j != i and nums[j] < nums[i].

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        rl = []
        for x in nums:
            i = 0
            counter = 0
            while len(nums) > i:
                if x > nums[i]:
                    counter += 1
                i += 1
            rl.append(counter)
            
        return rl