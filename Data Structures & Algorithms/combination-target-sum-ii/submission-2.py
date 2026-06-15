class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        candidates.append(-1)
        result = []

        def recursive(currCandidates, remaining, i) :
            if remaining == 0 :
                result.append(currCandidates.copy())
                return
            
            if remaining < 0 :
                return

            if candidates[i] == -1 :
                return

            currCandidates.append(candidates[i])
            recursive(currCandidates, remaining - candidates[i], i+1)
            currCandidates.pop()

            while candidates[i] == candidates[i+1] :
                i = i + 1
            
            if candidates[i] != candidates[i+1] :
                recursive(currCandidates, remaining, i+1)

        recursive([], target, 0)
        return result
            
            
            
            
        