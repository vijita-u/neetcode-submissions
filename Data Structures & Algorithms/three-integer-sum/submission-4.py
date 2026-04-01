class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # Avoid duplicates
        for cur, val in enumerate(nums):
            if cur > 0 and val == nums[cur-1]:  # first check to avoid out of bounds error
                continue # move to the next iteration

            l, r = cur+1, len(nums)-1
            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    # Only need to avoid duplicates when the target is reached
                    l += 1  # increment left first and later check if it is valid
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                    while r > l and nums[r] == nums[r+1]:
                        r -=1
        return res


         