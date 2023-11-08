#  my own solution passes some test case but not all

'''class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = collections.defaultdict(int) #fruittype -->count in basket
        l,total,res = 0,0,0
        for r in range (len(fruits)):
            count[fruits[r]] +=1
            total +=1

            while len(count)>2:
                f = fruits[1]
                count[f]-=1
                total -=1
                l +=1
                if not  count[f]:
                    count.pop(f) 

            res = max(res,total)
        return res''' 


class Solution:
  def totalFruit(self, tree: List[int]) -> int:
    ans = 0
    count = collections.defaultdict(int)

    l = 0
    for r, t in enumerate(tree):
      count[t] += 1
      while len(count) > 2:
        count[tree[l]] -= 1
        if count[tree[l]] == 0:
          del count[tree[l]]
        l += 1
      ans = max(ans, r - l + 1)

    return ans  
