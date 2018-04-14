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
