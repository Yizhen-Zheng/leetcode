from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        '''
        review union find
        7:48-8:52
        there will be cases looks like:
        J: A, B
        J: C, D (currently it seems to be different accounts)
        J: D, A (now it appears this can be merged)
        undirected graph
        cannot use name as keys!!!
        n: len(accounts)
        m: num of emails
        t: O(n*m)
        s: O(n*m)(dics, rec)
        '''
        n = len(accounts)
        degrees = defaultdict(set)
        adj = [set() for _ in range(n)]
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                degrees[email].add(i)  # build degree to node list
                adj[i].add(email)

        print(degrees)
        merged = defaultdict(set)
        visited = set()

        def dfs(cur_idx: int, belongs_to: int):
            if cur_idx in visited:
                return
            visited.add(cur_idx)
            # merged[belongs_to].add(cur_idx)# instead of adding idx, try directly add email
            for email in adj[cur_idx]:
                merged[belongs_to].add(email)
                neighbors = degrees[email]
                for neighbor in neighbors:
                    dfs(neighbor, belongs_to)
        for i in range(n):
            dfs(i, i)
        print(merged)
        # form res
        res = []
        for idx, emails in merged.items():
            res.append([accounts[idx][0], *sorted(list(emails))])
        return res

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        '''
        9:00-9:44
        '''
        class UnionFind:
            def __init__(self, size):
                self.parents = [i for i in range(size)]

            def union(self, x, y):
                # NOTE this was incorrect implemented, that's the reason it becomes
                # uf.union(uf.find(i), uf.find(neighbor))
                # instead of union(i,neighbor)
                self.parents[y] = self.find(x)
                return

            def find(self, x):
                if self.parents[x] != x:
                    # find x's parent's parent until root, and assign it
                    self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

        n = len(accounts)
        uf = UnionFind(n)
        degrees = defaultdict(set)
        adj = [set() for _ in range(n)]
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                degrees[email].add(i)  # build degree to node list
                adj[i].add(email)
        [print(degree)for degree in degrees.items()]
        print(adj)

        for i in range(n):
            for email in adj[i]:
                neighbors = degrees[email]
                for neighbor in neighbors:
                    uf.union(uf.find(i), uf.find(neighbor))
        print(uf.parents)
        ans = defaultdict(set)
        for i in range(n):
            parent = uf.find(i)
            _, *emails = accounts[i]
            ans[parent].update(emails)
        ans_list = []
        for i, emails in ans.items():
            ans_list.append([accounts[i][0], *sorted(emails)])
        print(ans)
        return ans_list

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        '''
        cleanup above
        '''
        class UnionFind:
            def __init__(self, size):
                self.parents = [i for i in range(size)]

            def union(self, x, y):
                uf.union(uf.find(x), uf.find(y)),
                return

            def find(self, x):
                if self.parents[x] != x:
                    # find x's parent's parent until root, and assign it
                    self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

        n = len(accounts)
        uf = UnionFind(n)
        adj = {}

        for i, (_, *emails) in range(n):
            for email in emails:
                if email in adj:
                    uf.union(i, adj[email])  # if we've seen this email previously, merge cur with prev
                adj[email] = i
        print(uf.parents)
        ans = defaultdict(set)
        for i in range(n):
            parent = uf.find(i)  # find its parent
            _, *emails = accounts[i]  # get child's emails
            ans[parent].update(emails)  # add child's email to parent
        ans_list = []
        for i, emails in ans.items():  # find name, convert format
            ans_list.append([accounts[i][0], *sorted(emails)])
        print(ans)
        return ans_list

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        '''
        solution
        '''
        class UnionFind:
            def __init__(self, size):
                self.parents = [i for i in range(size)]

            def union(self, x, y):
                # NOTE this was incorrect implemented before
                # self.parents[y] = self.find(x)  # incorrect
                self.parents[self.find(y)] = self.find(x)
                return

            def find(self, x):
                if self.parents[x] != x:
                    # find x's parent's parent until root, and assign it
                    self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

        n = len(accounts)
        uf = UnionFind(n)
        belongs_to = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in belongs_to:
                    # uf.union(uf.find(i), uf.find(belongs_to[email])) # for compensate incorrect
                    uf.union(i, belongs_to[email])
                belongs_to[email] = i  # assign parent
        [print(degree)for degree in belongs_to.items()]
        print(uf.parents)
        ans = defaultdict(list)
        for email, owner in belongs_to.items():
            ans[uf.find(owner)].append(email)  # add email to untimate parent
        ans_list = []
        for i, emails in ans.items():
            ans_list.append([accounts[i][0], *sorted(emails)])
        print(ans)
        return ans_list

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        '''
        DFS solution
        '''
        n = len(accounts)
        degrees = defaultdict(list)
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                degrees[email].append(i)  # build degree to node list

        print(degrees)
        merged = defaultdict(set)
        # if 2 email can be used to 'link' the same pair of accounts, we don't need to link them twice
        visited = set()

        def dfs(account_idx: int, belongs_to: int):
            if account_idx in visited:
                return
            visited.add(account_idx)
            # merged[belongs_to].add(cur_idx)# instead of adding idx, try directly add email
            for email_idx in range(1, len(accounts[account_idx])):
                email = accounts[account_idx][email_idx]
                merged[belongs_to].add(email)
                neighbors = degrees[email]
                for neighbor in neighbors:
                    dfs(neighbor, belongs_to)
        for i in range(n):
            dfs(i, i)
        print(merged)
        # form res
        res = []
        for idx, emails in merged.items():
            res.append([accounts[idx][0], *sorted(list(emails))])
        return res


t = [['A', 'a', 'b'], ['A', 'c', 'd'], ['A', 'd', 'a']]
# t = [['A', 'a', 'b'], ['A', 'b', 'c'], ['B', 'd'], ['A', 'e']]
t = [["Hanzo", "Hanzo2@m.co", "Hanzo3@m.co"],
     ["Hanzo", "Hanzo4@m.co", "Hanzo5@m.co"],
     ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co"],
     ["Hanzo", "Hanzo3@m.co", "Hanzo4@m.co"],
     ["Hanzo", "Hanzo7@m.co", "Hanzo8@m.co"],
     ["Hanzo", "Hanzo1@m.co", "Hanzo2@m.co"],
     ["Hanzo", "Hanzo6@m.co", "Hanzo7@m.co"],
     ["Hanzo", "Hanzo5@m.co", "Hanzo6@m.co"]]
r = Solution().accountsMerge(t)
print(r)
