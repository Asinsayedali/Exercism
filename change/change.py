from itertools import combinations_with_replacement
from typing import Iterator


def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    if target < 0:
        raise ValueError("target can't be negative")

    max_coins: int = 1 + target // min(coins)

    for i in range(max_coins):
        combinations: Iterator[tuple[int, ...]] = combinations_with_replacement(coins, i)
        for combination in combinations:
            if sum(combination) == target:
                return sorted(combination)

    raise ValueError("can't make target with given coins")
