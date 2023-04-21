import math


def degrees_to_rad(degrees: float) -> float:
    return degrees * math.pi / 180


def calculate_delta(a: float, b: float) -> float:
    return a - b


def calculate_mid_lat(lat1: float, lat2: float) -> float:
    return (lat1 + lat2) / 2


def power_by_second(value: float) -> float:
    return value**2


def calculate_distance(
    lat1: float, lon1: float, lat2: float, lon2: float, R: float = 360 * 60 / math.tau
) -> float:
    return math.sqrt(
        power_by_second(
            R
            * degrees_to_rad(calculate_delta(lon1, lon2)) 
            * math.cos(calculate_mid_lat(degrees_to_rad(lat1), degrees_to_rad(lat2)))
        )
        + power_by_second(
            R * calculate_delta(degrees_to_rad(lat1), degrees_to_rad(lat2))
        )
    )


print(calculate_distance(32.82950, -79.93021, 32.74412, -79.85226))
