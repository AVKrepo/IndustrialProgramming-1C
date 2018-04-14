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


class TestUnaryOperations(object):

    def test_unary_plus(self):
        code = "x = 5; print(+x)"
        assert compare_outputs(code)

    def test_unary_minus(self):
        code = "x = 5; y = -x; print(y)"
        assert compare_outputs(code)

    def test_unary_not(self):
        code = "x = True; print(not x)"
        assert compare_outputs(code)

    def test_unary_invert(self):
        code = "x = 25; y = ~x; print(+y)"
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

    def test_logical_and_with_not(self):
        code = "z = True and not False; print(z)"
        assert compare_outputs(code)

    def test_logical_and_with_jump(self):
        code = "z = False and True; print(z)"
        assert compare_outputs(code)


class TestComparisonOperators(object):

    def test_equal(self):
        code = "x = 1 == 2; print(x)"
        assert compare_outputs(code)

    def test_not_equal(self):
        code = "x = 1 != 2; print(x)"
        assert compare_outputs(code)

    def test_greater(self):
        code = "x = 1 > 2; print(x)"
        assert compare_outputs(code)

    def test_less(self):
        code = "x = 1 < 2; print(x)"
        assert compare_outputs(code)

    def test_greater_or_equal(self):
        code = "x = 1 >= 2; print(x)"
        assert compare_outputs(code)

    def test_less_or_equal(self):
        code = "x = 1 <= 2; print(x)"
        assert compare_outputs(code)

    def test_is(self):
        code = "x = 1 is 1; print(x)"
        assert compare_outputs(code)

    def test_is_not(self):
        code = "x = 1 is not 1; print(x)"
        assert compare_outputs(code)

    def test_list(self):
        code = "x = [1, 2, 4, 6]; print(x)"
        assert compare_outputs(code)

    def test_tuple(self):
        code = "x = (1, 2, 4); print(x)"
        assert compare_outputs(code)

    def test_in_list(self):
        code = "x = [1, 2, 4]; print(2 in x)"
        assert compare_outputs(code)

    def test_not_in_tuple(self):
        code = "x = (1, 2, 4); print(2 not in x)"
        assert compare_outputs(code)


class TestComplexArithmetic(object):

    def test_complex_arithmetic1(self):
        code = "z = False; z |= True; print(z or True and False)"
        assert compare_outputs(code)

    def test_complex_arithmetic2(self):
        code = "x, y = 20, 50 // 6; y **= 0.4; z = (x + y) * (y - 2); print(z + 1)"
        assert compare_outputs(code)




