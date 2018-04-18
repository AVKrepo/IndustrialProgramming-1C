from tests.utils import compare_outputs


class TestCases(object):

    def test_if_true(self):
        code = "x = True\nif x: print(1)"
        assert compare_outputs(code)

    def test_if_false_else(self):
        code = "x = False\nif x: print(1)\nelse: print(2)"
        assert compare_outputs(code)

    def test_if_true_else(self):
        code = "x = True\nif x: print(1)\nelse: print(2)"
        assert compare_outputs(code)

    def test_double_if1(self):
        code = "t = True\nif t:\n\tif t: print(1)"
        assert compare_outputs(code)

    def test_double_if2(self):
        code = "t, f = True, False\nif t:\n\tif f: print(1)\n\telse: print(2)"
        assert compare_outputs(code)

    def test_double_if3(self):
        code = "t, f = True, False\nif f: print(1)\nelse:\n\tif t: print(2)"
        assert compare_outputs(code)

    def test_double_if4(self):
        code = "t, f = True, False\nif f: print(1)\nelse:\n\tif f: print(2)\n\telse: print(3)"
        assert compare_outputs(code)


class TestCycles(object):

    def test_for_in_list(self):
        code = "for i in [1, 2]: print(i)"
        assert compare_outputs(code)

    def test_for_in_tuple(self):
        code = "for i in (1, 2, 5): print(i)"
        assert compare_outputs(code)
