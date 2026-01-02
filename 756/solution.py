class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # build a dict of first letter key to allowed sub sets
        allowed_d = {}
        for allow in allowed:
            key = (allow[0], allow[1])
            if key not in allowed_d:
                allowed_d[key] = []
                    
            allowed_d[key].append(allow[2])

        memo = {}

        return self.solve(0, bottom, "", allowed_d, memo)

    
    def solve(self, pos: int, bottom: str, above: str, allowed_d: dict, memo: dict) -> bool:
        # check if already computed
        if bottom in memo:
            return memo[bottom]

        # check if bottom is iterated through and above is completed
        if pos+1 == len(bottom):
            if len(above) != len(bottom) - 1:
                return False

            if len(above) == 1:
                memo[bottom] = True
                return True
            
            r = self.solve(0, above, "", allowed_d, memo)
            return r
        
        key = (bottom[pos], bottom[pos+1])
        result = False

        # check if there are any allowed lists for current letter
        allowed = allowed_d.get(key, None)
        if allowed is None:
            return False

        # for each allowed list, check if next in bottom string matches one
        for allow in allowed:
            # if sub problem is already true, just return
            if result is True:
                memo[bottom] = True
                return result
            
            # place letter in above and recursive
            result = self.solve(pos+1, bottom, "" + above + allow, allowed_d, memo)

        return result
        