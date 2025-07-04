class Solution:
    def reverse_linked_list_loop(self, linked_list):
        '''
        '''
        prev = None
        current = linked_list

        while current:
            temp = current['next']
            current['next'] = prev
            prev = current
            current = temp
        # return the new head
        return prev

    def reverse_linked_list_rec(self, linked_list: dict[dict]):
        '''
        '''
        def rec(prev, current):
            if not current:
                return prev
            temp = current['next']
            current['next'] = prev
            return rec(current, temp)

        return rec(None, linked_list)


t = {'val': 1, 'next': {'val': 2, 'next': {'val': 3, 'next': {'val': 4, 'next': {'val': 5, 'next': {'val': 6, 'next': None}}}}}}
# r = Solution().reverse_linked_list_loop(t)
r = Solution().reverse_linked_list_rec(t)
print(r)
