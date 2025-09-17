
from typing import List, Any

def chunk(values: List[Any], size: int) -> List[List[Any]]:
    """Split list into chunks of length size. Last chunk may be shorter."""
    if size <= 0:
        raise ValueError("size must be positive")
    result = []
    for i in range(0, len(values), size):
        result.append(values[i:i+size])
    return result


def running_total(start: int, values: List[int]) -> List[int]:
    """Return list of running totals starting from `start`."""
    result = []
    total = start
    for v in values:
        total += v
        result.append(total)
    return result


def index_of_first_at_least(values: List[int], target: int) -> int | None:
    """Return index of first element >= target, else None."""
    for i in range(len(values)):
        if values[i] >= target:
            return i
    return None
