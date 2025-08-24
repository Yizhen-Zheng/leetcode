from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        '''
        different name -> different person
        same name -> same or not same person
        common email -> proofed to have same name and be same person
        problem is cannot use name as dict key
        emails initially not sorted

        try brute force:NOT WORK
        '''
        n = len(accounts)
        table = defaultdict(list)
        ans = defaultdict(list)
        # key: str, val: lists of email
        # {name: [[emails],[emails]...]}
        for i in range(n):
            name = accounts[i][0]
            emails = accounts[i][1:]
            table[name].append(emails)

        def merge(name):
            email_arrs = table[name]
            m = len(email_arrs)
            merged = []  # [set1,set2...]
            for i in range(m):  # loop currently unmerged groups
                cur_email_arr = email_arrs[i]  # check each group of emails
                can_merge = False
                target_idx = -1
                for email in cur_email_arr:  # check each email, if there's common
                    for j in range(len(merged)):  # check existing groups
                        existing_set = merged[j]
                        if email in existing_set:
                            can_merge = True
                            target_idx = j  # store where we want to merge
                            break
                    if can_merge:  # keep checking email if nothing can merge
                        break
                if can_merge:
                    target_set = merged[target_idx]
                    for email in cur_email_arr:
                        target_set.add(email)
                else:  # nothing to merge, add new
                    new_group = set()
                    for email in cur_email_arr:
                        new_group.add(email)
                    merged.append(new_group)
            ans[name] = merged
            return

        def sort_email(name):
            merged_groups = ans[name]
            for i in range(len(merged_groups)):
                email_set = merged_groups[i]
                email_list = sorted(list(email_set))
                merged_groups[i] = email_list

        for name in table.keys():
            merge(name)
            sort_email(name)
        formatted_ans = []  # add name to first of list
        for name in ans.keys():  # for each name
            merged_groups = ans[name]
            for group in merged_groups:  # for every merged account, add name
                arr = [name]
                arr.extend(group)
                formatted_ans.append(arr)
        return formatted_ans

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        '''
        solution
        '''
        n = len(accounts)
        # a set or map of 'visited', prevent visiting an original account twice
        visited_accounts = [False]*n
        email_to_account_idx = defaultdict(list)
        res = []
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                email_to_account_idx[email].append(i)
        print(email_to_account_idx)

        # emails: path(set), idx: position in original accounts
        # (corresponding to idx in visited_accounts)
        def dfs(idx, emails: set):
            if visited_accounts[idx]:
                return
            visited_accounts[idx] = True
            # for an existing account, loop emails
            for i in range(1, len(accounts[idx])):
                email = accounts[idx][i]
                emails.add(email)
                for linked_account_idx in email_to_account_idx[email]:
                    dfs(linked_account_idx, emails)
        for i, account in enumerate(accounts):
            if visited_accounts[i]:
                continue
            name, email_path = account[0], set()
            dfs(i, email_path)
            res.append([name]+sorted(email_path))
        return res

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        '''
        solution
        asterisk to unpack list
        '''
        # N: original accounts number
        # like jump liked list, number on each idx represents idx's parent
        # initially: parents[x]=x
        class UnionFind:
            def __init__(self, N):
                self.parents = list(range(N))

            def union(self, child, parent):
                # merge
                # find child: get child's ultimate parent
                # update child's parent's parent to parent's ultimate parent
                self.parents[self.find(child)] = self.find(parent)

            def find(self, x):
                if x != self.parents[x]:
                    # find x -> find x's parent
                    # then update the parent as ultimate parent(flatten the tree)
                    self.parents[x] = self.find(self.parents[x])
                return self.parents[x]
        n = len(accounts)  # retrieve account through its original idx
        uf = UnionFind(n)  # each accounts belongs to itself as init
        table = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in table:  # there's a common email(identical key) added before current
                    uf.union(i, table[email])  # merge account
                    # acconut i now belongs to previously appeared email's account
                table[email] = i  # record email owned by which account
        print(uf.parents)
        ans = defaultdict(list)
        for email, account_idx in table.items():
            # group emails as merged group
            parent = uf.find(account_idx)  # for child, append email to its parent
            ans[parent].append(email)
        merged_accounts = []
        for account_idx, emails in ans.items():
            name = accounts[account_idx][0]
            merged_accounts.append([name]+sorted(emails))
        return merged_accounts


t = [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com",
                                                               "john00@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]

r = Solution().accountsMerge(t)
print(r)
