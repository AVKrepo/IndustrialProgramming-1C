from tests.utils import compare_outputs


class TestArithmetic(object):

    def test_assignment(self):
        code = "x = 1; print(x)"
        assert compare_outputs(code)

    def test_assignment_and_assignment(self):
        code = "x = y = 1; print(x, y)"
        assert compare_outputs(code)

    def test_double_assignment(self):
        code = "x, y = 1, 2; print(x, y)"
        assert compare_outputs(code)

    def test_binary_add(self):
        code = "x = 1; y = x + 4; print(y)"
        assert compare_outputs(code)

    def test_binary_subtract(self):
        code = "x = 1; y = x - 4; print(y)"
        assert compare_outputs(code)

    def test_binary_multiply(self):
        code = "x = 1; y = x * 4; print(y)"
        assert compare_outputs(code)

    def test_binary_power(self):
        code = "x = 2; y = x ** 4; print(y)"
        assert compare_outputs(code)

    def test_binary_floor_divide(self):
        code = "x = 9; y = x // 4; print(y)"
        assert compare_outputs(code)

    def test_binary_true_divide(self):
        code = "x = 9; y = x / 4; print(y)"
        assert compare_outputs(code)

    def test_binary_modulo(self):
        code = "x = 9; y = x % 4; print(y)"
        assert compare_outputs(code)

    def test_binary_lshift(self):
        code = "x = 1; y = x << 4; print(y)"
        assert compare_outputs(code)

    def test_binary_lrshift(self):
        code = "x = 1; y = x >> 4; print(y)"
        assert compare_outputs(code)

    def test_binary_and(self):
        code = "x = 1; y = x & 4; print(y)"
        assert compare_outputs(code)

    def test_binary_xor(self):
        code = "x = 1; y = x ^ 4; print(y)"
        assert compare_outputs(code)

    def test_binary_or(self):
        code = "x = 1; y = x | 4; print(y)"
        assert compare_outputs(code)
