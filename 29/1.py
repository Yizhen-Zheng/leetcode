import unittest


class BinaryArithmetic:
    def __init__(self):
        pass

    def add(self, a, b):
        mask = 0xFFFFFFFF
        while (b & 0xFFFFFFFF):
            temp = a
            a = a ^ b
            b = (temp & b) << 1
        res = a & mask
        if res & (1 << 31):
            res |= ~mask  # convert to py negative representation
        print(res)
        return res

    def subtract(self, a, b):
        not_b = ~b
        two_complement_b = self.add(not_b, 1)
        res = self.add(a, two_complement_b)
        return res

    def multiply(self, a, b):
        is_negative = (a < 0) ^ (b < 0)
        if a < 0:
            a = self.add(~a, 1)
            # a = -a
        if b < 0:
            b = self.add(~b, 1)
            # b = -b
        ans = 0
        while b:
            if b & 1:
                ans = self.add(ans, a)
            b >>= 1
            a <<= 1  # effectively left shift next to add, without effect ans
        if is_negative:
            ans = self.add(~ans, 1)
        return ans

    def divide(self, dividend, divisor):
        mininum = -(1 << 31)
        maxinum = (1 << 31)-1
        if dividend == mininum and divisor == mininum:
            return 1
        elif divisor == mininum:
            return 0
        elif dividend == mininum and divisor == -1:
            return maxinum
        elif dividend == mininum:
            buffer = divisor if divisor > 0 else -divisor
            dividend = dividend+buffer
            return self.divide_calculate(dividend, divisor) - (1 if divisor > 0 else -1)
        else:
            return self.divide_calculate(dividend, divisor)

    def divide_calculate(self, a, b):
        is_minus = (a < 0) ^ (b < 0)

        if a < 0:
            a = self.add(~a, 1)
            # a = -a
        if b < 0:
            b = self.add(~b, 1)
            # b = -b

        ans = 0
        for i in range(30, -1, -1):
            if (a >> i) >= b:
                ans |= 1 << i
                a = self.subtract(a, b << i)
                # a -= (b << i)
        if is_minus:
            ans = self.add(~ans, 1)
        return ans


class TestBinaryArithmetic(unittest.TestCase):
    """
    Test suite for the BinaryArithmetic class.
    """

    def setUp(self):
        """Set up a new instance of the class for each test."""
        self.arithmetic = BinaryArithmetic()

    def test_add_positives(self):
        """Test addition of two positive numbers."""
        self.assertEqual(self.arithmetic.add(5, 10), 15)
        self.assertEqual(self.arithmetic.add(0, 0), 0)
        self.assertEqual(self.arithmetic.add(100, 200), 300)

    def test_add_negatives(self):
        """Test addition of two negative numbers."""
        self.assertEqual(self.arithmetic.add(-5, -10), -15)
        self.assertEqual(self.arithmetic.add(-1, -1), -2)
        self.assertEqual(self.arithmetic.add(-100, -200), -300)

    def test_add_mixed_signs(self):
        """Test addition of positive and negative numbers."""
        self.assertEqual(self.arithmetic.add(10, -5), 5)
        self.assertEqual(self.arithmetic.add(-10, 5), -5)
        self.assertEqual(self.arithmetic.add(100, -100), 0)

    def test_add_with_zero(self):
        """Test addition with zero."""
        self.assertEqual(self.arithmetic.add(123, 0), 123)
        self.assertEqual(self.arithmetic.add(0, 123), 123)
        self.assertEqual(self.arithmetic.add(-123, 0), -123)
        self.assertEqual(self.arithmetic.add(0, -123), -123)

    def test_add_overflow(self):
        """Test 32-bit integer overflow behavior."""
        max_int = 0x7FFFFFFF  # 2147483647
        min_int = -0x80000000  # -2147483648
        # 2147483647 + 1 should wrap around to -2147483648
        self.assertEqual(self.arithmetic.add(max_int, 1), min_int)
        # -2147483648 + (-1) should wrap around to 2147483647
        self.assertEqual(self.arithmetic.add(min_int, -1), max_int)

    def test_subtract_positives(self):
        """Test subtraction of two positive numbers."""
        self.assertEqual(self.arithmetic.subtract(10, 5), 5)
        self.assertEqual(self.arithmetic.subtract(5, 10), -5)
        self.assertEqual(self.arithmetic.subtract(100, 100), 0)

    def test_subtract_negatives(self):
        """Test subtraction of two negative numbers."""
        self.assertEqual(self.arithmetic.subtract(-10, -5), -5)
        self.assertEqual(self.arithmetic.subtract(-5, -10), 5)
        self.assertEqual(self.arithmetic.subtract(-100, -100), 0)

    def test_subtract_mixed_signs(self):
        """Test subtraction of positive and negative numbers."""
        self.assertEqual(self.arithmetic.subtract(10, -5), 15)
        self.assertEqual(self.arithmetic.subtract(-10, 5), -15)

    def test_subtract_with_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(self.arithmetic.subtract(123, 0), 123)
        self.assertEqual(self.arithmetic.subtract(0, 123), -123)
        self.assertEqual(self.arithmetic.subtract(-123, 0), -123)
        self.assertEqual(self.arithmetic.subtract(0, -123), 123)

    def test_subtract_underflow(self):
        """Test 32-bit integer underflow behavior."""
        max_int = 0x7FFFFFFF
        min_int = -0x80000000
        # -2147483648 - 1 should wrap around to 2147483647
        self.assertEqual(self.arithmetic.subtract(min_int, 1), max_int)
        # 2147483647 - (-1) should wrap around to -2147483648
        self.assertEqual(self.arithmetic.subtract(max_int, -1), min_int)

    def test_multiply_positives(self):
        """Test multiplication of two positive numbers."""
        self.assertEqual(self.arithmetic.multiply(5, 10), 50)
        self.assertEqual(self.arithmetic.multiply(1, 100), 100)
        self.assertEqual(self.arithmetic.multiply(12, 12), 144)

    def test_multiply_negatives(self):
        """Test multiplication of two negative numbers."""
        self.assertEqual(self.arithmetic.multiply(-5, -10), 50)
        self.assertEqual(self.arithmetic.multiply(-1, -100), 100)
        self.assertEqual(self.arithmetic.multiply(-12, -12), 144)

    def test_multiply_mixed_signs(self):
        """Test multiplication of a positive and a negative number."""
        self.assertEqual(self.arithmetic.multiply(5, -10), -50)
        self.assertEqual(self.arithmetic.multiply(-1, 100), -100)
        self.assertEqual(self.arithmetic.multiply(12, -12), -144)

    def test_multiply_with_zero(self):
        """Test multiplication with zero."""
        self.assertEqual(self.arithmetic.multiply(123, 0), 0)
        self.assertEqual(self.arithmetic.multiply(0, 123), 0)
        self.assertEqual(self.arithmetic.multiply(-123, 0), 0)
        self.assertEqual(self.arithmetic.multiply(0, -123), 0)
        self.assertEqual(self.arithmetic.multiply(0, 0), 0)

    def test_multiply_overflow(self):
        """Test multiplication that would overflow a 32-bit integer."""
        # This is a simplified check. True overflow in multiplication is complex.
        # 65536 * 65536 = 4294967296, which is 2^32. In 32-bit signed math, this is 0.
        self.assertEqual(self.arithmetic.multiply(65536, 65536), 0)
        # 100000 * 100000 should result in a wrapped-around value
        self.assertEqual(self.arithmetic.multiply(100000, 100000), 1410065408)


if __name__ == '__main__':
    """
    This block allows the script to be run directly from the command line,
    which will execute the test suite.
    """
    unittest.main(verbosity=2)
