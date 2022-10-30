import big_o
import pytest

from main import (
    _sorted_append,
    _sorted_extend,
    insertion_sort,
    merge_sort,
)


@pytest.fixture
def test_cases():
    return {
        "normal": {
            "pre": [7, 12, 10, 7, 1, 6, 16, 18, 3, 5],
            "post": [1, 3, 5, 6, 7, 7, 10, 12, 16, 18],
        },
        "empty": {"pre": [], "post": []},
        "one_element": {"pre": [1], "post": [1]},
        "already_sorted": {
            "pre": [1, 3, 5, 6, 7, 7, 10, 12, 16, 18],
            "post": [1, 3, 5, 6, 7, 7, 10, 12, 16, 18],
        },
    }


class TestInternalMethods:
    def test_sorted_append(self):
        assert _sorted_append([1, 3], 2) == [1, 2, 3]

    def test_sorted_extend(self):
        assert _sorted_extend([1, 3], [2, 4]) == [1, 2, 3, 4]


class TestSortingAlgorithms:
    def test_insertion_sort(self, test_cases):
        for case in test_cases.keys():
            assert (
                insertion_sort(test_cases[case]["pre"])
                == test_cases[case]["post"]
            )


    def test_merge_sort(self, test_cases):
        for case in test_cases.keys():
            assert (
                merge_sort(test_cases[case]["pre"])
                == test_cases[case]["post"]
            )
"""
positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)


def test_appendion_sort_quadratic():
    best, _ = big_o.big_o(
        insertion_sort,
        positive_int_generator,
        n_repeats=30,
        min_n=10,
        max_n=1000,
    )
    assert "Quadratic" in str(best)
"""
