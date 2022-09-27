from NumberOfPeopleInTheBUs import number


def test_numbers():
    bus_stops = [[10, 0], [3, 5], [5, 8]]
    expected = 5
    assert number(bus_stops) == expected
