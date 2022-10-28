from main import (
    _sorted_insert,
    insertion_sort,
)
import big_o


def test_sorted_insert():
    tgt = [1, 3]
    _sorted_insert(tgt, 2)
    assert tgt == [1, 2, 3]


to_sort = [3, 1, 5, 2, 7, 7, 8]
ordered = sorted(to_sort)


def test_insertion_sort():
    assert insertion_sort(to_sort) == ordered


positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)


def test_insertion_sort_quadratic():
    best, _ = big_o.big_o(
        insertion_sort,
        positive_int_generator,
        n_repeats=30,
        min_n=10,
        max_n=1000,
    )
    assert "Quadratic" in str(best)
