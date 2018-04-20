from tests.utils import compare_outputs


class TestFunctions(object):

    def test_custom_print_function(self):
        code = "def f():\n\tprint(256)\n\nf()"
        assert compare_outputs(code)

    def test_function_one_argument(self):
        code = "def f(x):\n\treturn x ** 2\n\nprint(f(5))"
        assert compare_outputs(code)

    def test_function_two_arguments(self):
        code = "def mul_(x, y):\n\treturn x * y\n\nprint(mul_(5, 6))"
        assert compare_outputs(code)

    def test_function_two_arguments2(self):
        code = "def pow_(x, y):\n\treturn y ** x\n\nprint(pow_(5, 6))"
        assert compare_outputs(code)

    def test_function_two_arguments3(self):
        code = "def f(x, y):\n\treturn x ** x / y ** x\n\nprint(f(3, 5))"
        assert compare_outputs(code)
