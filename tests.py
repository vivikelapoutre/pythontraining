from conversions import mile_to_feet, convert


def test_function_converts_miles():
    assert mile_to_feet(1) == 5290
    assert mile_to_feet(0.1) == 528


def test_function_converts_km():
    assert int(convert(10)) == 6
    assert int(convert(1000)) == 621