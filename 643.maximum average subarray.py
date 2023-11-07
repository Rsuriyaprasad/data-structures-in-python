class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #sum for starting window
        sum = 0
        for i in range(k):
            sum = sum + nums[i]

        maxsum = sum
        i=0
        j=k
        while j < len(nums):
            sum  = sum - nums[i]
            sum  = sum + nums[j]
            maxsum = max(maxsum ,sum)
            i=i+1
            j=j+1
        return maxsum/k
