from mock import Mock

from decorators import cached

CACHE = dict()


@cached(cache=CACHE)
def foo(a, b):
    test_mock = Mock()
    test_mock(a, b)
    return a * b, test_mock


def test_simple_work():
    result, _ = foo(2, 2)
    assert result == 4


def test_double_execution():
    result, mock1 = foo(2, 4)
    result_1, mock2 = foo(2, 4)

    assert result == result_1 == 8
    assert mock1 == mock2
    assert not mock1.assert_called_once_with(2, 4)
