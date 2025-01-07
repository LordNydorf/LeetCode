class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        win_count = 0
        if k > len(arr):
            return max(arr)
        else:
            try:
                while win_count < k:
                    if arr[0] > arr[1]:
                        win_count += 1
                        del arr[1]
                    else:
                        win_count = 1
                        del arr[0]
            except IndexError:
                return arr[0]
            return arr[0]
