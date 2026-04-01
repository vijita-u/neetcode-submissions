class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        # populate prefix array
        pref_prod = 1
        for i, n in enumerate(nums):
            prefix[i] = pref_prod
            pref_prod *= n
        
        # populate suffix array
        suf_prod = 1
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = suf_prod
            suf_prod *= nums[i]
        
        # calculate product of each index in prefix and suffix array
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])

        return res