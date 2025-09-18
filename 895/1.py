from collections import defaultdict


class FreqStack:
    '''
    maybe ordered dict?
    or heap((freq,arr))?
    pop the most freq
    push will modify frequency
    HAHA! 
    20:30-20:50(after brewing about 3 days)
    the good is after poping, expose the next most frequency natually 
    '''

    def __init__(self):
        self.most_freq = 0
        self.val_to_freq = defaultdict(int)
        self.freq_to_val = defaultdict(list)  # maybe a set
        return

    def push(self, val: int) -> None:
        self.val_to_freq[val] += 1
        cur_freq = self.val_to_freq[val]
        self.freq_to_val[cur_freq].append(val)
        self.most_freq = max(cur_freq, self.most_freq)
        print(self.val_to_freq)
        print(self.freq_to_val)
        return

    def pop(self) -> int:
        cur_freq = self.most_freq
        elem = self.freq_to_val[cur_freq].pop()
        self.val_to_freq[elem] -= 1
        if not self.freq_to_val[cur_freq]:
            self.most_freq -= 1
        return elem
