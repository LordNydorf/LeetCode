class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        arr=[]
        min = 1e9
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]: 
                    if (i+j<min):
                        arr.clear()
                        arr.append(list1[i])
                        min = i+j
                    elif (i+j == min):
                        arr.append(list1[i])
        return arr
