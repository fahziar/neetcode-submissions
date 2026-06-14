class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Min string length > t
        # The shortest possible window is t
        if len(s) < len(t) : 
            return ""

        # the idea:
        # We create a window, starting from position 1 with size t.
        # and then we need to define how to slide the window:
        # How to slide:
        # 1. If the window contains all character in t:
        #.   a) check whether it is the shortest, update the current shortest if shorter than it
        #.   b) then try to slide the left border
        #.      i) the window is smaller than len(t), we also need to slide the right border
        # 2. If the window doesn't contains all the character, then what we need to do is move the left border
        # 3. End condition:
        #   a) The right window touch the end of s, and
        #   b) Current window doesn't contain every character in s
        

        currShortest = ""
        left = 0
        right = len(t) - 1

        while right < len(s) or left < right :
            print(f"{left},{right}")
            if right != len(s) :
                if self.isContains(s, left, right, t) :
                    if currShortest == "" or len(currShortest) > right - left + 1:
                        currShortest = s[left:right+1]
                    left += 1
                else :
                    right += 1
                
                if right == len(s) :
                    left += 1
            else :
                if self.isContains(s, left, right-1, t) :
                    if currShortest == "" or len(currShortest) > right - left:
                        currShortest = s[left:right]
                
                left += 1
        
        return currShortest

    
    def isContains(self, s, left, right, t) :
        # s: ADOBECODEBANC
        # t : ABC
        # left: 9
        # right : 12

        chars = defaultdict(int)

        for c in t :
            chars[c] += 1
        #chars[A] : 1
        #chars[B] : 1
        #charss[C] : 1
        
        for i in range(left, right + 1) :
            chars[s[i]] -= 1
        
        #chars[A] : 0
        #chars[B] : 0
        #chars[C] : 0
        #chars[N] : -1

        for char, count in chars.items() :
            if (count > 0) :
                return False
        
        return True
