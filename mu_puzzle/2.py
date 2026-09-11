class SolutionII:
    """given a input and a goal, check if the goal is reachable from the input"""

    def canDerive(self, start: str, target: str) -> bool:
        '''
        MIU system (GEB, Ch. 1)
        alphabet: M, I, U
        axiom: MI

        rules (fill these in yourself):
        1. xI     -> xIU
        2. Mx     -> Mxx
        3. xIIIx  -> xUx
        4. xUUx   -> xx
        (x = any substring)

        '''
        # a set for all dead ends
        dead_ends = set()
        can_reach = set()
        can_reach.add(start)  # <- target
        # based on the rule, if input does not contain M, it is impossible to reach the target if target contains M. So we can return False directly.
        if 'M' not in target:
            return False

        pass

    def nextStates(self, s: str) -> list[str]:
        '''
        TODO: given a string s, return all strings reachable by applying
        one rule one time (at any valid position in s).
        '''
        pass


r = SolutionII().canDerive('MI', 'MU')
print(r)
