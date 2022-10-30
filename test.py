"""
test.py
Patrick Applegate
29 October 2022

Tests the implementations of simple sorting algorithms given in main.py,
including checking their time complexity.
"""

import big_o  # type: ignore
import pytest

from main import (
    _sorted_append,
    _sorted_extend,
    insertion_sort,
    merge_sort,
    quicksort,
)


@pytest.fixture(name="cases")
def fixture_cases():
    """
    Sets up test cases for the sorting algorithms.
    """
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


@pytest.fixture(name="big_o_settings")
def fixture_big_o_settings():
    """
    Defines consistent settings for the big_o package.
    """
    return {
        "n_repeats": 30,
        "min_n": 1,
        "max_n": 10**3,
    }


# pylint: disable-next=invalid-name
def positive_integers(n):
    """
    Just a wrapper function, really.
    """
    return big_o.datagen.integers(n, 0, 10**4)


class TestInternalMethods:
    """
    Tests methods that shouldn't be used outside of the sorting algorithms.
    """
    def test_sorted_append(self):
        """
        Make sure we can append a single element.
        """
        assert _sorted_append([1, 3], 2) == [1, 2, 3]

    def test_sorted_extend(self):
        """
        Make sure that extending works.
        """
        assert _sorted_extend([1, 3], [2, 4]) == [1, 2, 3, 4]


class TestSortingAlgorithms:
    """
    Checks the sorting algorithms themselves.
    """
    def test_insertion_sort(self, cases):
        """
        Applies insertion sort to the different cases.
        """
        assert (
            insertion_sort(cases["even_length"]["pre"])
            == cases["even_length"]["post"]
        )
        assert (
            insertion_sort(cases["odd_length"]["pre"])
            == cases["odd_length"]["post"]
        )
        assert (
            insertion_sort(cases["already_sorted"]["pre"])
            == cases["already_sorted"]["post"]
        )
        assert (
            insertion_sort(cases["one_element"]["pre"])
            == cases["one_element"]["post"]
        )
        assert insertion_sort(cases["empty"]["pre"]) == cases["empty"]["post"]

    def test_merge_sort(self, cases):
        """
        Applies merge sort to the different cases.
        """
        assert (
            merge_sort(cases["even_length"]["pre"])
            == cases["even_length"]["post"]
        )
        assert (
            merge_sort(cases["odd_length"]["pre"])
            == cases["odd_length"]["post"]
        )
        assert (
            merge_sort(cases["already_sorted"]["pre"])
            == cases["already_sorted"]["post"]
        )
        assert (
            merge_sort(cases["one_element"]["pre"])
            == cases["one_element"]["post"]
        )
        assert merge_sort(cases["empty"]["pre"]) == cases["empty"]["post"]

    def test_quicksort(self, cases):
        """
        Applies quicksort to the different cases.
        """
        assert (
            quicksort(cases["even_length"]["pre"])
            == cases["even_length"]["post"]
        )
        assert (
            quicksort(cases["odd_length"]["pre"])
            == cases["odd_length"]["post"]
        )
        assert (
            quicksort(cases["already_sorted"]["pre"])
            == cases["already_sorted"]["post"]
        )
        assert (
            quicksort(cases["one_element"]["pre"])
            == cases["one_element"]["post"]
        )
        assert quicksort(cases["empty"]["pre"]) == cases["empty"]["post"]


class TestComplexity:
    """
    Ensures that the time complexity of the individual sorting algorithms
    matches our expectations.
    """
    def test_insertion_sort_quadratic(self, big_o_settings):
        """
        Insertion sort should be quadratic.
        """
        best, _ = big_o.big_o(
            insertion_sort,
            positive_integers,
            **big_o_settings,
        )
        assert "Quadratic" in str(best)

    def test_merge_sort_nlogn(self, big_o_settings):
        """
        Merge sort should be n log n.
        """
        best, _ = big_o.big_o(
            merge_sort,
            positive_integers,
            **big_o_settings,
        )
        assert "Linearithmic" in str(best)

    def test_quicksort_nlogn(self, big_o_settings):
        """
        Quicksort should also be n log n.
        """
        best, _ = big_o.big_o(
            quicksort,
            positive_integers,
            **big_o_settings,
        )
        assert "Linearithmic" in str(best)
