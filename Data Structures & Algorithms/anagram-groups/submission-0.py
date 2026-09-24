class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)

        for i in strs:
            s = str(sorted(i))
            out[s].append(i)

        return list(out.values())