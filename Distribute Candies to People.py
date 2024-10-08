class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        k = 0
        while candies > 0:
            if candies >= (k+1):
                candies -= (k+1)
                ans[k % num_people] += k + 1
            else:
                ans[k % num_people] += candies
                candies = 0
            k += 1
        return ans
