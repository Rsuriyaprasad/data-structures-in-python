class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
      if m*n!= len(original):
          return []

      sol = []

      for i in range (0,len(original),n):
          sol.append(original[i:i+n])

      return sol   
                
