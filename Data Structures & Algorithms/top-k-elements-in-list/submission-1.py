class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = defaultdict(int)

        for i in nums:
            out[i]+=1

        dsc = {k: v for k, v in sorted(out.items(), key=lambda item: item[1], reverse=True)}
        return list(dsc.keys())[:k]