class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        # Append the strings to hashmap      
        for s in strs:
            sign = self.createSignature(s)
            anagrams[sign].append(s)
        
        # Iterate through the hashmap
        res = []
        for signature, strings in anagrams.items():
            res.append(strings)

        return res
        
    def createSignature(self, s: str) -> tuple:
        count = [0] * 26
        for c in s:
            idx = ord(c.lower()) - ord('a')
            count[idx] += 1
        return tuple(count)