class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        # Store counts in the dict a.k.a hash table
        for n in nums:
            freq[n] += 1
        
        # Create a bucket to store the frequencies
        bucket = [[] for _ in range(len(nums))]
        for num, count in freq.items():
            bucket[count-1].append(num)

        # Iterate backwards to get the top k-frequent elements
        res=[]
        for i in range(len(bucket)-1, -1, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res
        