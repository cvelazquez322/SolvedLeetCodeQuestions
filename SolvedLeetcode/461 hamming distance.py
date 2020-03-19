# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xx = list(f'{x:032b}')
        yy = list(f'{y:032b}')
        i = 0
        counter = 0
        while(i < len(xx)):
            if xx[i] != yy[i]:
                counter +=1
            i += 1
        return counter