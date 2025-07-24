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

        countS, countT = {}, {}  #using a dict as I do lot of fetching & it retrieves in constant time

        for i in range(len(s)): #O(n)
            countS[s[i]] = 1 + countS.get(s[i], 0) #O(1)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS: #O(m), m<=n so worst case O(n)
            if countS[c] != countT.get(c,0): #O(1)
                return False
        return True

        # O(n) + O(m) or O(n) + O(n) = O(2n) 
        # time complexity is O(n+m)
        # space complexity is O(1)

