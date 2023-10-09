lass Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numset:
                length =0
                # length is sequence
                while(n+length) in numset:
                    length+=1
                longest =max(length,longest)
        return longest
