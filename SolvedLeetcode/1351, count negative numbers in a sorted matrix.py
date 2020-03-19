# Given a m * n matrix grid which is sorted in non-increasing order 
# both row-wise and column-wise. 

# Return the number of negative numbers in grid.

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        if len(grid) == 0:
            return 0
        for alist in grid:
            for aint in alist:
                if aint < 0:
                    count += 1
        return count