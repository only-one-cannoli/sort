from copy import deepcopy
from typing import List


def _sorted_append(target: List[float], to_insert: float) -> List[float]:
    """
    Inserts to_insert into target such that the result remains sorted.  Assumes
    that target is sorted!
    """
    where = 0
    try:
        for element in target:
            if to_insert < element:
                break
            else:
                where += 1
    except IndexError:
        where = len(target)
    target.insert(where, to_insert)

    return target


def insertion_sort(target: List[float]) -> List[float]:
    """
    Insertion sort.
    """
    try:
        ordered = [target[0]]
    except IndexError:
        return target

    for element in target[1:]:
        _sorted_append(ordered, element)

    return ordered


def _sorted_extend(list1: List[float], list2: List[float]) -> List[float]:
    """
    Extends list1 with the contents of list2.  Assumes that both lists are
    already sorted!
    """
    ordered = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] <= list2[0]:
            ordered.append(list1.pop(0))
        else:
            ordered.append(list2.pop(0))
    if len(list1) > 0:
        ordered.extend(list1)
    elif len(list2) > 0:
        ordered.extend(list2)

    return ordered


def merge_sort(target: List[float]) -> List[float]:
    """
    Merge sort.
    """
    if len(target) < 1:
        return []

    split = [[element] for element in target]

    while len(split) > 1:

        if len(split) % 2 == 1:
            split.append([])

        split = [
            _sorted_extend(split[i], split[i + 1])
            for i in range(0, len(split) - 1, 2)
        ]

    return split[0]


def quicksort(target: List[float]) -> List[float]:
    """
    Quicksort.
    """
    if len(target) < 2:
        return target

    pivot = target[-1]
    target = target[:-1]

    less = []
    greater_or_equal = []
    for element in target:
        if element < pivot:
            less.append(element)
        else:
            greater_or_equal.append(element)

    return quicksort(less) + [pivot] + quicksort(greater_or_equal)
