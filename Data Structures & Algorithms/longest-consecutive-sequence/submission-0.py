class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in elements:  # start of a new sequence
                count = 1
                next = n+1
                while next in elements:
                    count += 1
                    next += 1
                longest = max(longest, count)
        return longest

                    
                