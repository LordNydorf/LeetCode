class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        list1=[]
        for i in range(1,2001):
            list1.append(i)
        for j in arr:
            if j in list1:
                list1.remove(j)
        return list1[k-1]
