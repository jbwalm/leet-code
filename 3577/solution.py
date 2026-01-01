class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        clen = len(complexity)

        unlockables = []
        for i in range(clen):
            unlockables_for_i = []
            for j in range(i):
                if complexity[j] < complexity[i]:
                    unlockables_for_i.append(j)
            
            # check if unlockables for i is empty, if it is nothing can unlock so we can return 0
            if i != 0 and len(unlockables_for_i) == 0:
                return 0

            unlockables.append(unlockables_for_i)

        mask = 1
        memo = {}

        permutation_count = self.findPermutations(mask, memo, unlockables, complexity, 1, clen)

        MOD = 10**9 + 7
        return permutation_count % MOD

    def findPermutations(self, mask, memo, unlockables, complexity, p, clen) -> int:
        if (mask, p) in memo:
            return memo[(mask, p)]
        
        if (p == clen):
            return 1
        
        count = 0
        for i in range(clen):
            if (mask >> i) & 1:
                continue

            i_can_unlock = False
            for j in unlockables[i]:
               if (mask >> j) & 1:
                    i_can_unlock = True
                    break
            
            if i_can_unlock:
                count += self.findPermutations(mask | (1 << i), memo, unlockables, complexity, p+1, clen)

        memo[(mask, p)] = count
        return count