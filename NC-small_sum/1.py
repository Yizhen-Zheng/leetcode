'''
链接：https://www.nowcoder.com/questionTerminal/edfe05a1d45c4ea89101d936cac32469
来源：牛客网

数组小和的定义如下：...

例如，数组 s = [1, 3, 5, 2, 4, 6] ，在 s[0] 的左边小于或等于 s[0] 的数的和为 0 ； 在 s[1] 的左边小于或等于 s[1] 的数的和为 1 ；在 s[2] 的左边小于或等于 s[2] 的数的和为 1+3=4 ；在 s[3] 的左边小于或等于 s[3] 的数的和为 1 ；
在 s[4] 的左边小于或等于 s[4] 的数的和为 1+3+2=6 ；在 s[5] 的左边小于或等于 s[5] 的数的和为 1+3+5+2+4=15 。所以 s 的小和为 0+1+4+1+6+15=27
给定一个数组 s ，实现函数返回 s 的小和

输入描述:
第一行有一个整数N。表示数组长度
接下来一行N个整数表示数组内的数

输出描述:
一个整数表示答案
'''


def smaller_sumI(n: int, nums: list[int]) -> int:
    '''
    naive solution: n^2
    total sum = left result + right result
    f(len-1) = f((0 -> len-1)//2) + f((len - 1)//2 -> len)
    '''
    if len(nums) <= 1:
        return 0

    def count_merge(a, b):
        '''this assume a and b are sorted'''
        sum_bothside = 0
        ptr_a = 0
        ptr_b = 0
        prev = 0
        merged = []
        while ptr_a < len(a) and ptr_b < len(b):
            num_a = a[ptr_a]
            num_b = b[ptr_b]
            if num_a <= num_b:
                prev += num_a
                ptr_a += 1
                merged.append(num_a)
            else:
                sum_bothside += prev
                ptr_b += 1
                merged.append(num_b)
        for idx in range(ptr_b, len(b)):
            sum_bothside += prev
            merged.append(b[idx])
        for idx in range(ptr_a, len(a)):
            merged.append(a[idx])
        return (sum_bothside, merged)
    unit_len = 1
    total = 0
    while unit_len < len(nums):
        for i in range(0, len(nums), unit_len << 1):
            l = i
            m = i+unit_len
            r = m+unit_len
            a = nums[l:m]
            b = nums[m:r]
            new_sum, merged = count_merge(a, b)
            total += new_sum
            nums[l:r] = merged
        unit_len <<= 1
    return total


def smaller_sum(n: int, nums: list[int]) -> int:
    '''
    naive solution: n^2
    total sum = left result + right result
    f(len-1) = f((0 -> len-1)//2) + f((len - 1)//2 -> len)
    '''
    if len(nums) <= 1:
        return 0

    def count_merge(a, b):
        '''this helper assumes a and b are sorted'''

        sum_bothside = 0
        ptr_a = 0
        prev = 0
        merged = []
        for ptr_b in range(0, len(b)):
            while ptr_a < len(a) and a[ptr_a] <= b[ptr_b]:
                prev += a[ptr_a]
                merged.append(a[ptr_a])
                ptr_a += 1
            sum_bothside += prev
            merged.append(b[ptr_b])
        # print(ptr_b) # note that after a for loop,
        # we can still access the idx_variable defined within for idx_variable in range(...)
        for idx in range(ptr_a, len(a)):
            # any remaining in a, like a=[5,6,8] b=[1,2,3], ptr_a will be 0
            merged.append(a[idx])
        return (sum_bothside, merged)

    total = 0

    def rec(nums):
        if len(nums) <= 1:
            return 0
        l = 0
        m = len(nums)//2
        r = len(nums)
        a = nums[l:m]
        b = nums[m:r]
        sum_a = rec(a)
        sum_b = rec(b)
        new_sum, merged = count_merge(a, b)
        return sum_a+sum_b+new_sum
    total = rec(nums)
    return total


# t = [0]
# t = [-1, 3, 9, 4, 0]
t = [1, 3, 5, 2, 4, 6]
t = [9, 5, 100]
t = [100, 100]
t = [100, 10, 1]
# t = [100, 7,  2, 2, 2]
r = smaller_sum(len(t), t)
print(r)
