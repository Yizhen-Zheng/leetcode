
# class BitsetI:

#     def __init__(self, size: int):
#         self.values = [0]*((size+31)//32)
#         self.size = size
#         self.count_bits = 0

#     def fix(self, idx: int) -> None:

#         (bucket_idx, bit_idx) = self.get_idx(idx)
#         self.values[bucket_idx] |= (1 << bit_idx)
#         self.count_bits += 1

#     def unfix(self, idx: int) -> None:
#         bucket_idx, bit_idx = self.get_idx(idx)
#         mask = self.manual_not(1 << bit_idx)
#         self.values[bucket_idx] &= mask
#         self.count_bits -= 1

#     def flip(self) -> None:
#         for i in range(len(self.values)):
#             self.values[i] ^= ((1 << 32)-1)
#         self.count_bits = self.size-self.count_bits
#         return

#     def all(self) -> bool:
#         for i in range(len(self.values)-1):
#             if self.values[i] != 0xFFFFFFFF:
#                 return False
#         last_bucket = self.values[-1]
#         for i in range(self.size % 32):
#             if not last_bucket & 1:
#                 return False
#             last_bucket >>= 1

#     def one(self) -> bool:
#         return sum(self.values) > 0

#     def count(self) -> int:
#         return self.count_bits

#     def toString(self) -> str:
#         res=[]


class Bitset:
    def __init__(self, size=128):
        '''
        manual ceil: a/b -> (a+b-1)/b
        '''
        self.values = [0]*((size+31)//32)
        self.size = size
        self.count = 0

    def flip_bit(self, num):
        '''
        args:
            num: the number to store
            value: 0 or 1, unset or set
        '''
        self.check_input(num)

        (bucket_idx, bit_idx) = self.get_idx(num)
        target_digit = self.get_bit(num)
        if target_digit:
            self.count -= 1
        else:
            self.count += 1

        self.values[bucket_idx] ^= (1 << bit_idx)
        return

    def set_bit(self, num):
        self.check_input(num)

        (bucket_idx, bit_idx) = self.get_idx(num)
        self.values[bucket_idx] |= (1 << bit_idx)
        self.count += 1

    # def unset_bit(self, num):
    #     target_digit = self.get_bit(num)
    #     if target_digit:
    #         self.flip_bit(num)

    def unset_bit(self, num):
        self.check_input(num)

        bucket_idx, bit_idx = self.get_idx(num)
        mask = self.manual_not(1 << bit_idx)
        self.values[bucket_idx] &= mask
        self.count -= 1

    def get_bit(self, num):
        self.check_input(num)
        (bucket_idx, bit_idx) = self.get_idx(num)
        target_digit = (self.values[bucket_idx] >> bit_idx) & 1
        return target_digit

    def get_idx(self, num):
        '''
        args: 
            num: the number to store
        return: 
            bucket_idx: the integer's idx,
            bit_idx: the digit to offset, [0,31], inclusive
        '''
        self.check_input(num)

        if num > self.size-1:
            return -1
        bucket_idx = num//32
        bit_idx = num % 32
        return (bucket_idx, bit_idx)

    def manual_not(self, num, bits=32):
        # self.check_input(num)
        '''create a bit mask and use it to flip number'''
        return num ^ ((1 << bits)-1)

    def count_set_bits(self):
        return self.count

    def __str__(self):
        '''String representation showing bit pattern'''
        bits = []
        for i in range(self.size):
            bits.append(str(self.get_bit(i)))
        return ''.join(reversed(bits))  # Show MSB first

    def __repr__(self):
        return f"Bitset(size={self.size}, set_bits={self.count_set_bits()})"

    def check_input(self, num):
        if num < 0 or num > self.size-1:
            raise IndexError


bs = Bitset()
r = bs.manual_not(0xFFFFFFFF)
print(r)
r = bs.set_bit(1)

r = bs.get_bit(1)
print(r)
r = bs.unset_bit(1)

r = bs.get_bit(1)
print(r)


def test():

    # Comprehensive Tests
    print("Testing Bitset Implementation")
    print("=" * 50)

    # Test 1: Basic operations
    print("Test 1: Basic Operations")
    bs = Bitset(32)

    # Initially all bits should be 0
    assert bs.get_bit(0) == 0
    assert bs.get_bit(31) == 0
    assert bs.count_set_bits() == 0

    # Set some bits
    bs.set_bit(0)
    bs.set_bit(5)
    bs.set_bit(31)

    assert bs.get_bit(0) == 1
    assert bs.get_bit(1) == 0
    assert bs.get_bit(5) == 1
    assert bs.get_bit(31) == 1
    assert bs.count_set_bits() == 3

    print("✓ Basic set/get operations work")

    # Test 2: Flip operations
    print("\nTest 2: Flip Operations")
    bs.flip_bit(0)  # Should become 0
    bs.flip_bit(1)  # Should become 1

    assert bs.get_bit(0) == 0
    assert bs.get_bit(1) == 1
    assert bs.count_set_bits() == 3

    print("✓ Flip operations work")

    # Test 3: Unset operations
    print("\nTest 3: Unset Operations")
    bs.unset_bit(5)  # Should become 0
    bs.unset_bit(1)  # Should become 0

    assert bs.get_bit(5) == 0
    assert bs.get_bit(1) == 0
    assert bs.count_set_bits() == 1  # Only bit 31 should be set

    print("✓ Unset operations work")

    # Test 4: Large bitset (multi-bucket)
    print("\nTest 4: Multi-bucket Operations")
    large_bs = Bitset(100)

    # Set bits across different buckets
    large_bs.set_bit(0)    # First bucket
    large_bs.set_bit(32)   # Second bucket
    large_bs.set_bit(64)   # Third bucket
    large_bs.set_bit(99)   # Last valid bit

    assert large_bs.get_bit(0) == 1
    assert large_bs.get_bit(32) == 1
    assert large_bs.get_bit(64) == 1
    assert large_bs.get_bit(99) == 1
    assert large_bs.count_set_bits() == 4

    print("✓ Multi-bucket operations work")

    # Test 5: Edge cases and bounds checking
    print("\nTest 5: Bounds Checking")
    try:
        bs.get_bit(-1)
        assert False, "Should have raised IndexError"
    except IndexError:
        print("✓ Negative index properly rejected")

    try:
        bs.get_bit(32)  # Size is 32, so valid range is 0-31
        assert False, "Should have raised IndexError"
    except IndexError:
        print("✓ Out of bounds index properly rejected")

    # Test 6: Utility methods
    print("\nTest 6: Utility Methods")
    bs.clear_all()
    assert bs.count_set_bits() == 0
    assert not bs.any_bits_set()

    bs.set_all()
    assert bs.count_set_bits() == 32
    assert bs.all_bits_set()
    assert bs.any_bits_set()

    print("✓ Utility methods work")

    # Test 7: String representation
    print("\nTest 7: String Representation")
    small_bs = Bitset(8)
    small_bs.set_bit(0)
    small_bs.set_bit(2)
    small_bs.set_bit(7)

    # Bits: 76543210 -> 10000101
    expected = "10000101"
    assert str(small_bs) == expected
    print(f"✓ String representation: {str(small_bs)}")

    # Test 8: Manual NOT function
    print("\nTest 8: Manual NOT Function")
    bs_test = Bitset(8)

    # Test manual_not function
    assert bs_test.manual_not(0b10101010, 8) == 0b01010101
    assert bs_test.manual_not(0, 8) == 255
    assert bs_test.manual_not(255, 8) == 0

    print("✓ Manual NOT function works correctly")

    # Performance test
    print("\nTest 9: Performance Test")
    perf_bs = Bitset(10000)

    # Set every 100th bit
    for i in range(0, 10000, 100):
        perf_bs.set_bit(i)

    assert perf_bs.count_set_bits() == 100
    print("✓ Large bitset performance test passed")

    print("\n" + "=" * 50)
    print("All tests passed! ")


if __name__ == '__main__':
    test()
