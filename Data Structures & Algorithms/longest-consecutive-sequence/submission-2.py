class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # We are going to visit each number atmost twice

        # Convert the nums list into a set for constant time lookup
        n = set(nums)
        # Keep track of LCS
        LCS = 0

        for num in nums:
            seq = 1
            # If num start of seq
            if (num-1) not in n:
                # Check for consecutive numbers
                while (num+seq) in n:
                    seq += 1
            # Update LCS
            LCS = max(LCS, seq)
        
        return LCS

                    
                