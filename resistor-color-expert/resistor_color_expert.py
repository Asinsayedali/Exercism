tolerance_values = {
    "grey": "±0.05%",
    "black": "±0.5%",
    "violet": "±0.1%",
    "blue": "±0.25%",
    "green": "±0.5%",
    "brown": "±1%",
    "red": "±2%",
    "gold": "±5%",
    "silver": "±10%"
}

list_of_colors=["black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white"]
def value(color):
    return list_of_colors.index(color)


def resistor_label(colors):
    tolerance_color = colors[-1]
    if len(colors) == 4:
        result= (
            10 * value(colors[0]) + value(colors[1])
        ) * 10 ** value(colors[2])
    elif len(colors) == 5:
        result = (
            100 * value(colors[0]) + 10 * value(colors[1]) + value(colors[2])
        ) * 10 ** value(colors[3])
    else:
        return "0 ohms"

    prefix = ""
    if result >= 1_000_000_000:
        result /= 1_000_000_000
        prefix = "giga"
    elif result >= 1_000_000:
        result /= 1_000_000
        prefix = "mega"
    elif result >= 1_000:
        result /= 1_000
        prefix = "kilo"
    return (
        f"{result:g} "
        f"{prefix}ohms "
        f"{tolerance_values[tolerance_color]}"
    )