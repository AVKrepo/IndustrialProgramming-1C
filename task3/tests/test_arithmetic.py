from tests.utils import compare_outputs


class TestAssignment(object):

    def test_assignment(self):
        code = "x = 1; print(x)"
        assert compare_outputs(code)

    def test_assignment_and_assignment(self):
        code = "x = y = 1; print(x, y)"
        assert compare_outputs(code)

    def test_double_assignment(self):
        code = "x, y = 1, 2; print(x, y)"
        assert compare_outputs(code)


class TestBinaryOperations(object):

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

    def test_complex_operations(self):
        code = "x = 1; y = x | 4; print(y)"
        assert compare_outputs(code)


class TestLogicalOperations(object):

    def test_logical_or(self):
        code = "z = False or True; print(z)"
        assert compare_outputs(code)

    def test_logical_or_with_jump(self):
        code = "z = True or False; print(z)"
        assert compare_outputs(code)

    def test_logical_and(self):
        code = "z = True and False; print(z)"
        assert compare_outputs(code)

    def test_logical_and_with_jump(self):
        code = "z = False and True; print(z)"
        assert compare_outputs(code)





