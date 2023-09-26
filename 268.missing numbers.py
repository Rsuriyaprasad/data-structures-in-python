class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      # solution 1
        return (len(nums)*(len(nums)+1))//2-sum(nums)
      # solution 2
        return reduce(lambda x,y: x ^ y, list(range(len(nums)+1)) + nums)
