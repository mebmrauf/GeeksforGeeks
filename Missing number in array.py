# https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1

class Solution:
    def missingNumber(self, array):
        n = len(array) + 1
        expectedSum = n * (n + 1) // 2
        actualSum = sum(array)
        
        return expectedSum - actualSum
