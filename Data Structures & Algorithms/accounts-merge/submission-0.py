class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        parent = [i for i in range(len(accounts))]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])   # path compression
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)

            if px != py:
                parent[py] = px

        # email -> account index
        emailToAcc = {}

        # union accounts having same email
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in emailToAcc:
                    union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i

        # root -> emails
        emailGroup = {}

        for email, accIdx in emailToAcc.items():
            root = find(accIdx)

            if root not in emailGroup:
                emailGroup[root] = []

            emailGroup[root].append(email)

        res = []

        for root, emails in emailGroup.items():
            name = accounts[root][0]
            res.append([name] + sorted(emails))

        return res