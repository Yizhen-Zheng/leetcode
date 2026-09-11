class Solution:
    """just try is its possible to reach MU from MI"""

    def canDeriveMUFromMI(self) -> bool:
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

        TODO: implement search (BFS/DFS/whatever) over strings reachable
        from `start` by applying the rules, and return whether `target`
        is reachable.

        Minor TODO: use f-string or str.join() instead of stringA+stringB
        '''
        # a set for all dead ends
        dead_ends = set()
        can_reach = set()
        can_reach.add('MU')  # <- target
        final_reachable = self.nextStates('MI', can_reach, dead_ends)
        return 'MU' in final_reachable

    def nextStates(self, s: str, can_reach: set, dead_ends: set) -> list[str]:
        '''
        given a string s, return all strings reachable by applying
        one rule one time (at any valid position in s).
        it is aBFS
        '''
        next_states = []
        # if s is already in can_reach, return
        if s in can_reach:
            return next_states
        # if s is already in dead_ends, return
        if s in dead_ends:
            return next_states

        # use rule 1
        if s.endswith('I'):
            new_s = s + 'U'
            if new_s not in can_reach and new_s not in dead_ends:
                can_reach.add(new_s)
                next_states.append(new_s)
        # use rule 2
        if s.startswith('M'):
            new_s = 'M' + s[1:] + s[1:]
            if new_s not in can_reach and new_s not in dead_ends:
                can_reach.add(new_s)
                next_states.append(new_s)
        # use rule 3
            # find all occurrences of 'III' in s
        idx = s.find('III')
        while idx != -1:
            new_s = s[:idx] + 'U' + s[idx+3:]
            if new_s not in can_reach and new_s not in dead_ends:
                can_reach.add(new_s)
                next_states.append(new_s)
            idx = s.find('III', idx + 1)
        # use rule 4
        idx = s.find('UU')
        while idx != -1:
            new_s = s[:idx] + s[idx+2:]
            if new_s not in can_reach and new_s not in dead_ends:
                can_reach.add(new_s)
                next_states.append(new_s)
            idx = s.find('UU', idx + 1)

        # if no new states can be generated, add s to dead_ends
        if not next_states:
            dead_ends.add(s)

        # for each new state, recursively call nextStates and collect final reachable states
        collect_final_reachable = set()
        for new_s in next_states:
            final_reachable = self.nextStates(new_s, can_reach, dead_ends)
            collect_final_reachable.update(final_reachable)
        return list(collect_final_reachable)


r = Solution().canDeriveMUFromMI()
print(r)
