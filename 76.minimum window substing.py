'''class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT,window = {},{}
        for c in t:
            countT[c] = 1+countT.get(c,0)

        have,need =0,len(countT)
        res,resLen = [-1,-1],float("infinity")
        l=0
        for r in range(len(s)):
            c=s[r]
            window[c]= 1+window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have +=1
            while have == need :
                #update our result
                if(r-l+1)<resLen:
                    res=[l,r]
                    resLen = (r-l+1)
                    #pop from the left from the window
                    window[s[l]] -=1
                    if s[l] in countT and window[s[l]] < countT[s[l]]:
                        have -=1
                    l+=1
            l,r = res
            return s[l:r+1] if resLen != float("infinity") '''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        needstr = collections.defaultdict(int)
        for ch in t:
            needstr[ch] += 1
        needcnt = len(t)
        res = (0, float('inf'))
        start = 0
        for end, ch in enumerate(s):
            if needstr[ch] > 0:
                needcnt -= 1
            needstr[ch] -= 1
            if needcnt == 0:
                while True:
                    tmp = s[start]
                    if needstr[tmp] == 0:
                        break
                    needstr[tmp] += 1
                    start += 1
                if end - start < res[1] - res[0]:
                    res = (start, end)
                needstr[s[start]] += 1
                needcnt += 1
                start += 1
          return '' if res[1] > len(s) else s[res[0]:res[1]+1]
