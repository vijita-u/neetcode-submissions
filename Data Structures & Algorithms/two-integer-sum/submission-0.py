class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = dict()

        for i, n in enumerate(nums):
            pair = target - n
            if pair in pairs:
                return [pairs[pair], i]
            else:
                pairs[n] = i