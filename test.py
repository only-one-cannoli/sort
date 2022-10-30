import big_o
import pytest

from main import (
    _sorted_append,
    _sorted_extend,
    insertion_sort,
    merge_sort,
    quicksort,
)


@pytest.fixture
def test_cases():
    return {
        "even_length": {
            "pre": [7, 12, 10, 7, 1, 6, 16, 18, 3, 5],
            "post": [1, 3, 5, 6, 7, 7, 10, 12, 16, 18],
        },
        "odd_length": {
            "pre": [7, 12, 10, 7, 1, 6, 16, 18, 3],
            "post": [1, 3, 6, 7, 7, 10, 12, 16, 18],
        },
        "already_sorted": {
            "pre": [1, 3, 5, 6, 7, 7, 10, 12, 16, 18],
            "post": [1, 3, 5, 6, 7, 7, 10, 12, 16, 18],
        },
        "one_element": {"pre": [1], "post": [1]},
        "empty": {"pre": [], "post": []},
    }


class TestInternalMethods:
    def test_sorted_append(self):
        assert _sorted_append([1, 3], 2) == [1, 2, 3]

    def test_sorted_extend(self):
        assert _sorted_extend([1, 3], [2, 4]) == [1, 2, 3, 4]


class TestSortingAlgorithms:
    def test_insertion_sort(self, test_cases):
        assert insertion_sort(test_cases["even_length"]["pre"]) == test_cases["even_length"]["post"]
        assert insertion_sort(test_cases["odd_length"]["pre"]) == test_cases["odd_length"]["post"]
        assert insertion_sort(test_cases["already_sorted"]["pre"]) == test_cases["already_sorted"]["post"]
        assert insertion_sort(test_cases["one_element"]["pre"]) == test_cases["one_element"]["post"]
        assert insertion_sort(test_cases["empty"]["pre"]) == test_cases["empty"]["post"]

    def test_merge_sort(self, test_cases):
        assert merge_sort(test_cases["even_length"]["pre"]) == test_cases["even_length"]["post"]
        assert merge_sort(test_cases["odd_length"]["pre"]) == test_cases["odd_length"]["post"]
        assert merge_sort(test_cases["already_sorted"]["pre"]) == test_cases["already_sorted"]["post"]
        assert merge_sort(test_cases["one_element"]["pre"]) == test_cases["one_element"]["post"]
        assert merge_sort(test_cases["empty"]["pre"]) == test_cases["empty"]["post"]

    def test_quicksort(self, test_cases):
        assert quicksort(test_cases["even_length"]["pre"]) == test_cases["even_length"]["post"]
        assert quicksort(test_cases["odd_length"]["pre"]) == test_cases["odd_length"]["post"]
        assert quicksort(test_cases["already_sorted"]["pre"]) == test_cases["already_sorted"]["post"]
        assert quicksort(test_cases["one_element"]["pre"]) == test_cases["one_element"]["post"]
        assert quicksort(test_cases["empty"]["pre"]) == test_cases["empty"]["post"]


def positive_integers(n):
    return big_o.datagen.integers(n, 0, 10 ** 4)

@pytest.fixture
def big_o_settings():
    return {
        "n_repeats": 30,
        "min_n": 1,
        "max_n": 10 ** 3,
    }

class TestComplexity:
    def test_insertion_sort_quadratic(self, big_o_settings):
        best, _ = big_o.big_o(
            insertion_sort,
            positive_integers,
            **big_o_settings,
        )
        assert "Quadratic" in str(best)

    def test_merge_sort_nlogn(self, big_o_settings):
        best, _ = big_o.big_o(
            merge_sort,
            positive_integers,
            **big_o_settings,
        )
        assert "Linearithmic" in str(best)

    def test_quicksort_nlogn(self, big_o_settings):
        best, _ = big_o.big_o(
            quicksort,
            positive_integers,
            **big_o_settings,
        )
        assert "Linearithmic" in str(best)
