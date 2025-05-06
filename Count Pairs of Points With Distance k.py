class Solution:
  def countPairs(self, coordinates: List[List[int]], k: int) -> int:
    data, res = {}, 0
    for v in coordinates:
      x1, y1 = v[0], v[1]
      for delta in range(k + 1):
        x, y = delta ^ x1, (k - delta) ^ y1
        if (x, y) in data:
          res += data[(x, y)]
      data[(x1, y1)] = data.get((x1, y1), 0) + 1
    return res
