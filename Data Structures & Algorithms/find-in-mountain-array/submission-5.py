class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        A = mountainArr
        l,r = 0, A.length()-1
        while l<r:
            m = (l+r)//2
            if A.get(m) < A.get(m+1):
                l = m+1
            else:
                r = m
        peak = l 
        l,r = 0, peak
        while l<=r:
            m = (l+r)//2
            if A.get(m) == target:
                return m
            elif A.get(m) > target:
                r = m-1
            else:
                l = m+1
               
        l,r = peak+1, A.length()-1
        while l<=r:
            m = (l+r)//2
            if A.get(m) == target:
                return m
            elif A.get(m) > target:
                l = m+1
            else:
                r = m- 1
        return -1         

                       