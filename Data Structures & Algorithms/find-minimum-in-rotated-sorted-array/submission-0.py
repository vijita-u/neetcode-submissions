class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        ans = nums[0]
        while l <= r:
            # If array already sorted
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break
            mid = (l + r) // 2
            ans = min(nums[mid], ans)
            if nums[mid] >= nums[l]:  # left-half sorted
                l = mid + 1
            else:
                r = mid - 1
        return ans

