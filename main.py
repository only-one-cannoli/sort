from typing import List


def _sorted_insert(target: List[float], to_insert: float) -> None:
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


def insertion_sort(target: List[float]) -> List[float]:
    """
    Insertion sort.
    """
    ordered = [target[0]]
    for element in target[1:]:
        _sorted_insert(ordered, element)

    return ordered
