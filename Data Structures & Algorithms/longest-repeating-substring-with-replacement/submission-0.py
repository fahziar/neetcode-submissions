class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        longestStreak = 0

        # iteration 1
        # "XYYX"
        # "^"

        while right < len(s) :
            count = {}
            for i in range(left, right + 1) :
                if s[i] not in count :
                    count[s[i]] = 0
                count[s[i]] += 1
            
            if len(count) > 1 :
                longestFrequency = max(count, key=count.get)
                count.pop(longestFrequency)
                
                replacements = 0
                for char, charCount in count.items() :
                    replacements += charCount
                
                if replacements > k :
                    left += 1
                else :
                    longestStreak = max( longestStreak, right - left + 1)
                    right += 1
            else :
                longestStreak = max( longestStreak, right - left + 1)
                right += 1
    
        return longestStreak



