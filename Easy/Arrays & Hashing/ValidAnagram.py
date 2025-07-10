class Solution:
    def isAnagram_(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
        # brute force solution
        # we can sort & compare
        # but time complexity will be O(nlogn + mlogm)
        # space complexity will be O(1) or O(n+m)

    def isAnagram__(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

        # python's inbuilt datastructure that counts things automatically
        # it has the same time & space complexity as the above solution

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True

        # time complexity is O(n+m)
        # space complexity is O(1)

