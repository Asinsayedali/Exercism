from itertools import combinations_with_replacement
from typing import Iterator


def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    if target < 0:
        raise ValueError("target can't be negative")
    if not target:
        return []

    max_coins = 1 + target // min(coins)
    coins = sorted(coins)
    for i in range(1, max_coins):
        combinations = combinations_with_replacement(coins, i)
        for combination in combinations:
            if sum(combination) == target:
                return sorted(combination)

    raise ValueError("can't make target with given coins")
