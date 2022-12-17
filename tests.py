from NumberOfPeopleInTheBUs import number
from ParseNiceInt import get_age
from TwoToOne import longest


def test_numbers():
    bus_stops = [[10, 0], [3, 5], [5, 8]]
    expected = 5
    assert number(bus_stops) == expected


def test_parse_int():
    text = "6 years old"
    expected = 6
    assert get_age(text) == expected


def test_longest():
    assert longest("abcdefg", "hijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz"
    assert longest("abcdefghijklmnopqrstuvwxyz", "abcdefg") == "abcdefghijklmnopqrstuvwxyz"
    assert longest("abcdefg", "hijklmnopqrstuvwxyzabcdefg") == "abcdefghijklmnopqrstuvwxyz"
    assert longest("abcd", "efgh") == "abcdefgh"
    assert longest("abcd", "dcba") == "abcd"
    assert longest("abcd", "") == "abcd"
    assert longest("", "") == ""
    assert longest("a", "") == "a"
