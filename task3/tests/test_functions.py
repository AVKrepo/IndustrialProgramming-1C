from tests.utils import compare_outputs


class TestFunctions(object):

    def test_custom_print_function(self):
        code = "def f():\n\tprint(256)\n\nf()"
        assert compare_outputs(code)

    def test_function(self):
        code = "def f(x):\n\treturn x ** 2\n\nprint(f(5))"
        assert compare_outputs(code)

