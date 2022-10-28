from main import (
    _sorted_insert,
    insertion_sort,
)

to_sort = [3, 1, 5, 2, 7, 7, 8]
ordered = sorted(to_sort)

def test_sorted_insert():
    tgt = [1, 3]
    _sorted_insert(tgt, 2)
    assert tgt == [1, 2, 3]

def test_insertion_sort():
    assert insertion_sort(to_sort) == ordered

