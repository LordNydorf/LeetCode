class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        stack = [-1]
        arr += [0]
        for i in range(len(arr)):                           
            while arr[i] < arr[stack[-1]]:                  
                mid = stack.pop()
                num = arr[mid]
                right = i
                left = stack[-1]
                res += num * (right-mid) * (mid-left)
            stack.append(i)
        return res % (10**9+7)
