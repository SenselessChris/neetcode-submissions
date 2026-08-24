class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}
        for x in range(len(s)):
            count_s[s[x]] = 1 + count_s.get(s[x], 0)
            count_t[t[x]] = 1 + count_t.get(t[x], 0)
        return count_s == count_t


