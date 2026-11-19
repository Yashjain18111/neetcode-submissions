class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sor="".join(sorted(s))
        tor="".join(sorted(t))
        if tor==sor:
            return True
        return False



        