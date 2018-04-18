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

    def test_for_i_sum(self):
        code = "sum_= 0\nfor i in range(5):\n\tprint(i)\n\tsum_ += i\nprint(sum_, i)"
        assert compare_outputs(code)

    def test_double_for(self):
        code = "for i in range(8):\n\tfor j in range(9):\n\t\tprint(i * j)"
        assert compare_outputs(code)

    def test_while(self):
        code = "i = 0\nwhile i < 10:\n\tprint(i)\n\ti += 1"
        assert compare_outputs(code)

    def test_while_break(self):
        code = "i = 0\nwhile True:\n\tprint(i)\n\ti += 1\n\tif i >= 5: break"
        assert compare_outputs(code)

    def test_for_continue(self):
        code = "for i in range(10):\n\tif i % 2 == 1: print(i)\n\telse: print(i % 2)"
        assert compare_outputs(code)
