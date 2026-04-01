class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        freq = [[] for _ in range(len(nums))]

        # Count
        for n in nums:
            counts[n] += 1
        # Group the counts
        for number, count in counts.items():
            freq[count-1].append(number)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) >= k:
                    return res
        