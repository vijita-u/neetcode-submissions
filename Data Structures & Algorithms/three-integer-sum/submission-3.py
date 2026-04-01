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
                    l += 1  # increment left first and later check if it is valid
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res


        res = []
        # Sort the list
        nums.sort()  # in-place

        for i, first in enumerate(nums):
            # Check if same value as the prev and ensure it doesn't go out of bounds for the first element
            while i > 0 and nums[i-1] == nums[i]:
                continue # Take the next element as the first
            # If the current is unique
            l = i+1
            r = len(nums)-1
            target = 0 - first
            
            while l < r:
                while (l-1) > 0 and l < r and nums[l] == nums[l-1]:
                    l += 1
                while (r+1) < len(nums)-1 and r > l and nums[r] == nums[r+1]:
                    r -= 1
                sum_pair = nums[l] + nums[r]
                if sum_pair > target:
                    r -= 1
                elif sum_pair < target:
                    l += 1
                else:
                    res.append([first, nums[l], nums[r]])
                    l += 1
                    r -= 1
            return res


         