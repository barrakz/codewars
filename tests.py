from NumberOfPeopleInTheBUs import number
from ParseNiceInt import get_age


def test_numbers():
    bus_stops = [[10, 0], [3, 5], [5, 8]]
    expected = 5
    assert number(bus_stops) == expected


def test_parse_int():
    text = "6 years old"
    expected = 6
    assert get_age(text) == expected
