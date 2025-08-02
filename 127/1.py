from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        '''
        different by a single char
        wordList: unique 
        all has same len
        brute force: rec all(maybe possible)
        22min, not work, no duplication / path record
        O(2^^N)
        maybe: sort by difference from end, maek graph somehow
        m: word len
        n: dict len
        '''
        def compare(a, b):  # O(m)
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
            return count

        def find(cur):  # O(n*m)
            explore = []
            for word in wordList:
                if compare(word, cur) == 1:
                    explore.append(word)
            return explore

        def rec(path_len, cur_word, visited: set):
            if cur_word == endWord:
                return path_len
            if path_len > len(wordList):
                return float('inf')
            visited.add(cur_word)
            min_path = float('inf')
            next_step = find(cur_word)
            print(path_len)
            for word in next_step:
                if word not in visited:
                    min_path = min(min_path, rec(path_len+1, word, visited.copy()))

            return min_path
        res = rec(1, beginWord, set())  # total path len, at least one (begin itself)
        return res if res != float('inf') else 0

    def ladderLengthI(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        '''
        try mark as visited
        if traverse by layer work?
        about 1 hours, not solved
        '''
        m = len(beginWord)
        visited = ''.ljust(m, '#')
        if endWord not in wordList:
            return 0

        def compare(a, b):  # O(m)
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
            return count

        def find(cur, word_list):  # O(n*m)
            explore = []
            for i in range(len(word_list)):
                if compare(word_list[i], cur) == 1:
                    explore.append(word_list[i])
                    word_list[i] = visited
            return explore

        q = deque([(beginWord, 1, wordList)])

        while q:
            print(len(q))
            cur, path_len, remain = q.popleft()
            print(path_len, remain.count('###'), len(remain))
            if cur == endWord:
                return path_len

            next_remain = remain.copy()
            explore = find(cur, next_remain)
            for next_word in explore:
                q.append((next_word, path_len+1, next_remain.copy()))
        return 0

    def ladderLengthI(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        '''
        follow solution
        t:
            q: up to n elems(with visited to prevent duplication)

        t:O(m^2*n)
        s:O(n)(set: n, q: n)
        '''
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        q = deque([beginWord])
        visited = set()
        path_len = 1
        while q:  # O(n)
            q_size = len(q)
            for i in range(q_size):  # just segment layers
                word = q.popleft()
                if word == endWord:
                    return path_len
                for j in range(len(word)):  # O(m)
                    for k in range(26):  # O(1)
                        char = chr(ord('a')+k)
                        word_arr = list(word)
                        word_arr[j] = char
                        new_word = ''.join(word_arr)  # O(m)
                        if (new_word in wordList) and (not new_word in visited):
                            q.append(new_word)
                            visited.add(new_word)
            path_len += 1
        return 0

    def ladderLengthI(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        '''
        BFS, set, and lookup table
        'ab' -> 'a_': 'ab', '_b': 'ab'
        why normal q not work: 
        for every iteration, need to iterate the whole wordList(n*m) to find next step to calculate
        using a dict to store precalculated perms
        t: O(m*n*m + m*n) = O(m^2*n)
        s: O(m*n) (dict: O(m*n), q:n, visited:n)
        '''
        if endWord not in wordList:
            return 0
        m = len(beginWord)
        visited = set()
        word_dict = defaultdict(list)
        for word in wordList:  # O(n)
            for i in range(m):  # O(m)
                word_idx_arr = list(word)
                word_idx_arr[i] = '_'
                word_idx = ''.join(word_idx_arr)  # O(m)
                word_dict[word_idx].append(word)
        q = deque([(beginWord, 1)])
        # queue: contains at most n words(since we have visited)
        while q:  # O(n)
            cur, path_len = q.popleft()
            if cur == endWord:
                return path_len
            for i in range(m):  # try all position in word, O(m)
                cur_arr = list(cur)
                cur_arr[i] = '_'
                next_word_idx = ''.join(cur_arr)
                for next_word in word_dict[next_word_idx]:
                    if next_word not in visited:
                        q.append((next_word, path_len+1))
                        visited.add(next_word)
        return 0


t = ('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"])
t = ('qa', 'sq', ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb",
     "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"])

r = Solution().ladderLengthI(t[0], t[1], t[2])
print(r)
