import AOC2016Day4Classes as AoC
import pytest


class TestRoom:

    def test_number_of_occurrences_sorted(real_room: str):
        r = AoC.Room(real_room)
        r.number_of_occurrences_sorted()
        number_occurences = r.occurrences_sorted_dict
        assert number_occurences["a"] == 5

    def test_calculate_checksum_returns_checksum(real_room: str):
        r = AoC.Room(real_room)
        r.number_of_occurrences_sorted()
        checksum_to_test = r.calculate_checksum()
        assert checksum_to_test == "abxyz"


@pytest.fixture
def real_room():
    return "aaaaa-bbb-z-y-x-123[abxyz]"
