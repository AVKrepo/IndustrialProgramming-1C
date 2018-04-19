from tests.utils import compare_outputs


class TestContainers(object):

    def test_list(self):
        code = "x = [1, 2, 4, 6]; print(x)"
        assert compare_outputs(code)

    def test_tuple(self):
        code = "x = (1, 2, 4); print(x)"
        assert compare_outputs(code)

    def test_set(self):
        code = "x = {1, 2, 5}; print(x)"
        assert compare_outputs(code)

    def test_map(self):
        code = "x = {1:2, 3:4, 5:6}\nprint(x)"
        assert compare_outputs(code)

    def test_list_slice(self):
        code = "x = [1, 2, 3]\nprint(x[1:2])"
        assert compare_outputs(code)

    def test_list_slice_step(self):
        code = "x = list(range(10))\nprint(x[-1:0:-1])"
        assert compare_outputs(code)

    def test_unpacking_kwargs(self):
        code = "x = {'sep':'\t', 'end':''}\nprint(1, 2, **x)"
        assert compare_outputs(code)

    def test_unpacking_args(self):
        code = "x = (1, 2, 3)\nprint(*x)"
        assert compare_outputs(code)

    def test_unpacking_args_kwargs(self):
        code = "args = (1, 2, 3)\nkwargs = {'sep':'\t', 'end':''}\nprint(*args, **kwargs)"
        assert compare_outputs(code)

    # def test_list_generator(self):
    #     code = "x = [i ** 2 for i in range(10)]\nprint(x)"
    #     assert compare_outputs(code)
