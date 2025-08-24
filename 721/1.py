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
            parent = uf.find(account_idx)  # for child account, find its ultimate parent
            ans[parent].append(email)  # put email to destination account
        merged_accounts = []
        for account_idx, emails in ans.items():
            name = accounts[account_idx][0]
            merged_accounts.append([name]+sorted(emails))
        return merged_accounts

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        '''
        try review dfs
        t: O(E log E)(e: email number)
            (but in dfs, there'll be duplicated visit same email more than one times, but immediately return without any further exploration)
        s: O(E)(for table size and stack depth)
        '''
        n = len(accounts)
        # build graph
        email_to_account_id = defaultdict(list)
        for i, emails in enumerate(accounts):  # O(E)
            for j in range(1, len(emails)):
                email = emails[j]
                email_to_account_id[email].append(i)
        # travel every original accounts
        used = [False]*n  # visit every account once

        def dfs(account_idx, email_path: set):
            # do nothing with already visited account
            if used[account_idx]:
                return
            # mark current visited
            used[account_idx] = True
            # try 'explore' every email of current account
            for i in range(1, len(accounts[account_idx])):
                email = accounts[account_idx][i]
                email_path.add(email)
                for linked_account_idx in email_to_account_id[email]:
                    dfs(linked_account_idx, email_path)

        ans = []
        for i in range(0, len(accounts)):  # O(N)
            if not used[i]:
                merged_emails = set()
                dfs(i, merged_emails)
                name = accounts[i][0]
                ans.append([name]+sorted(merged_emails))
        return ans

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        '''
        review unionfind
        UnionFind: Inverse Ackermann function, considered as const time
        t: O(E log E)(e: email number)
        s: O(E)(for table size)
        '''
        class UnionFind:
            def __init__(self, N):
                self.parents = [i for i in range(N)]

            def union(self, child, parent):  # O(N)
                # merge
                parent_of_child = self.find(child)
                parent_of_parent = self.find(parent)
                self.parents[parent_of_child] = parent_of_parent
                return

            def find(self, x):  # O(N)
                # find ultimate parent
                p = self.parents[x]
                if p != x:
                    p = self.find(p)
                self.parents[x] = p  # update to ultimate parent
                return p
        n = len(accounts)
        uf = UnionFind(n)
        email_to_account_idx = defaultdict(int)
        # i*j=O(number_of_emails)
        # union: O(1)
        for i in range(n):  # for existing accounts
            for j in range(1, len(accounts[i])):  # for connected emails of account
                email = accounts[i][j]
                if email in email_to_account_idx:
                    # email_to_account_idx[email]: another account linked to the same email
                    # means they can be merged
                    uf.union(i, email_to_account_idx[email])
                email_to_account_idx[email] = i  # update
        # one way to merge, this need set for trying to adding same email multiple times
        # account_idx_to_emails = defaultdict(set)
        # for i in range(n):
        #     parent_account_idx = uf.find(i)  # which merged account should go
        #     for j in range(1, len(accounts[i])):  # add email to destination
        #         account_idx_to_emails[parent_account_idx].add(accounts[i][j])

        # another way to merge:
        account_idx_to_emails = defaultdict(list)
        for email, child_account_idx in email_to_account_idx.items():  # O(number_of_accounts)
            parent_account_idx = uf.find(child_account_idx)  # O(1)
            account_idx_to_emails[parent_account_idx].append(email)

        # convert dict to list
        ans = []
        # overall: E log E
        # (the bigger one account gets, the less for loop loops)
        # (the more accounts, the less time in sort)
        for account_idx, emails in account_idx_to_emails.items():  # O(number_of_accounts)
            name = accounts[account_idx][0]
            ans.append([name]+sorted(emails))  # O(number_of_emails log number_of_emails)
        return ans


t = [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com",
                                                               "john00@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]

t = [["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"], ["Ethan", "Ethan5@m.co",
                                                                                                                  "Ethan4@m.co", "Ethan0@m.co"], ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"], ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]


r = Solution().accountsMerge(t)
print(r)
