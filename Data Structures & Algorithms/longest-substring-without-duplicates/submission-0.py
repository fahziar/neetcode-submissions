class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        
        i = 0
        j = 0
        maxlen = 0
        currlen = 0

        while i < len(s) and j < len(s):
            if s[j] not in chars :
                chars.add(s[j])
                j += 1
                currlen += 1
            else :
                if s[i] in chars :
                    chars.remove(s[i])
                i += 1
                currlen -= 1
            
            maxlen = max(currlen, maxlen)
        
        return maxlen

