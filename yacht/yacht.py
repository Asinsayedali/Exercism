from collections import Counter

YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"

CATEGORY_SCORES = {
    ONES: 1,
    TWOS: 2,
    THREES: 3,
    FOURS: 4,
    FIVES: 5,
    SIXES: 6,
    CHOICE: None
}


def score(dice, category):
    dice_count = Counter(dice)
    unique_dice = set(dice)

    if category == YACHT:
        return 50 if len(unique_dice) == 1 else 0

    if category in CATEGORY_SCORES:
        return dice_count[CATEGORY_SCORES[category]] * CATEGORY_SCORES[category] if CATEGORY_SCORES[category] else sum(
            dice)

    if category == FULL_HOUSE:
        if len(unique_dice) == 2 and 3 in dice_count.values():
            return sum(dice)

    if category == FOUR_OF_A_KIND:
        for num, count in dice_count.items():
            if count >= 4:
                return num * 4

    if category == LITTLE_STRAIGHT:
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0

    if category == BIG_STRAIGHT:
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0

    return 0
