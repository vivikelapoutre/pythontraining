FEET_PER_MILE = 5280


def mile_to_feet(distance_in_miles: float):
    return distance_in_miles * FEET_PER_MILE


def convert(a):
    return a / 1609344


if __name__ == "__main__":
    distance_in_km = 50

    distance_in_miles = convert(distance_in_km)
    print(f"{distance_in_km} km is {distance_in_miles} mijl")

    distance_in_feet = mile_to_feet(distance_in_miles)
    print(f"{distance_in_miles} mijl is {distance_in_feet} feet")