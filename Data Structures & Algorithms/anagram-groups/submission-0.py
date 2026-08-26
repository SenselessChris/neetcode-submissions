class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            signature = "".join(sorted(word))
            seen.setdefault(signature, []).append(word)
        return list(seen.values())