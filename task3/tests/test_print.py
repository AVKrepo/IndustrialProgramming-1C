from tests.utils import compare_outputs


class TestPrint(object):

    def test_print_int(self):
        code = "print(1)"
        assert compare_outputs(code)

    def test_print_float(self):
        code = "print(3.14)"
        assert compare_outputs(code)

    def test_print_str(self):
        code = "print('Hello, world!')"
        assert compare_outputs(code)

    def test_print_two_args(self):
        code = "print('Hello,', 'world!')"
        assert compare_outputs(code)

    def test_print_three_args(self):
        code = "print('hello', 1, 3.14)"
        assert compare_outputs(code)

    def test_print_with_kwarg(self):
        code = "print('hello ', end='world')"
        assert compare_outputs(code)

    def test_print_with_multiple_kwargs(self):
        code = "print('hello,', 'my dear ', sep='\t', end='world')"
        assert compare_outputs(code)

    def test_print_with_invalid_kwarg(self):
        code = "print(alabab='alabab')"
        assert compare_outputs(code)

    def test_double_print(self):
        code = """print(1); print(2)"""
        assert compare_outputs(code)
