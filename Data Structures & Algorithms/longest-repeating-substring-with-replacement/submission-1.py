class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        longestStreak = 0

        while right < len(s):
            counter = {}

            for i in range(left, right + 1) :
                if s[i] not in counter :
                    counter[s[i]] = 1
                else :
                    counter[s[i]] += 1
                
            if len(counter) > 1 :
                charWithMostFrequency = max(counter, key=counter.get)
                counter.pop(charWithMostFrequency)

                replacements = 0
                for char, count in counter.items() :
                    replacements += count
                
                if replacements <= k :
                    longestStreak = max(longestStreak, right-left+1)
                    right += 1
                else :
                    left += 1
            else :
                longestStreak = max(longestStreak, right-left+1)
                right += 1
            
        return longestStreak


                    


