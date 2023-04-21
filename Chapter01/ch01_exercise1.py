def sum_from_float_list(the_list: list[float]) -> float:
    if len(the_list) == 1:
        return the_list[0]
    else:
        return the_list[0] + sum_from_float_list(the_list[1:])


def exercise_1(
    v: list[float] = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
) -> float:
    return sum_from_float_list(v) / len(v)


def variant_2(
    v: list[float] = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
) -> float:
    return sum(v) / len(v)

print(variant_2())