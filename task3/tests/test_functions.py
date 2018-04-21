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

    def test_function_two_arguments4(self):
        code = "def f(x, y):\n\treturn x ** x / y ** x\n\nprint(f(3, 5), f(4, 6))"
        assert compare_outputs(code)

    def test_function_two_arguments5(self):
        code = "def f(x, y):\n\treturn x ** x / y ** x\n\nprint(f(x=3, y=5), f(y=4, x=6))"
        assert compare_outputs(code)

    def test_function_second_argument_optional(self):
        code = "def f(x, y=5):\n\treturn x * x / (y % x)\n\nprint(f(4))"
        assert compare_outputs(code)

    def test_function_arguments_optional(self):
        code = "def f(x, y=5, z=10):\n\treturn z + x ** y\n\nprint(f(3, 4))"
        assert compare_outputs(code)

    def test_function_arguments_optional2(self):
        code = "def f(x, y=5, z=10):\n\treturn z + x ** y\n\nprint(f(3))"
        assert compare_outputs(code)

    def test_function_arguments_optional3(self):
        code = "def f(x, y=5, z=10):\n\treturn z + x ** y\n\nprint(f(3) * f(2, 3) / f(1) / f(1, 2, 5))"
        assert compare_outputs(code)

    def test_function_arguments_optional4(self):
        code = "def f(x=1, y=2, z=3):\n\treturn z + x ** y\n\nprint(f(z=126))"
        assert compare_outputs(code)

    def test_two_functions(self):
        code = "def range_(to, from_=0, step=1):\n" \
               "\treturn range(from_, to, step)\n\n" \
               "def sum_(args):\n\treturn sum(list(args))\n\n" \
               "print(sum_(range_(20)) + sum_(range_(2, 23, 2)))"
        assert compare_outputs(code)

    # def test_function_global_argument(self):
    #     code = "x = 25\n\ndef f(y): return x + y\n\nprint(f(6))"
    #     print(exec(code))
    #     assert compare_outputs(code)
