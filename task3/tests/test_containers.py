from tests.utils import compare_outputs


class TestContainers(object):

    def test_list(self):
        code = "x = [1, 2, 4, 6]; print(x)"
        assert compare_outputs(code)

    def test_tuple(self):
        code = "x = (1, 2, 4); print(x)"
        assert compare_outputs(code)