# https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1

class Solution:
    def subArraySum(self, arr, target):
        start = 0
        currentSum = 0
        
        for end in range(len(arr)):
            currentSum += arr[end]
            
            while currentSum > target and start <= end:
                currentSum -= arr[start]
                start += 1
            
            if currentSum == target:
                return [start + 1, end + 1]
        
        return [-1]
