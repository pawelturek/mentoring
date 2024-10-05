import os.path
import string

class EncryptedData:
    """loading encrypted data from txt file"""

    def __init__(self, file_txt: str):
        self.lines_object_list = []
        self.file_txt = file_txt
        self.local_dir = r'/'
        self.file_path = os.path.join(self.local_dir, self.file_txt)
        print(self.file_path)

        try:
            with open(self.file_path, "r") as file:
                for line in file.readlines():
                    room_object = Room(line.strip())
                    self.lines_object_list.append(room_object)
        except IOError:
            raise IOError("{} not found in {}".format(self.file_txt, self.local_dir))



        #def sum_sector_id(self):



class Room:

    def __init__(self, line: str):
        self.occurrences_dict = {q: 0 for q in string.ascii_lowercase[:26]}
        self.occurrences_sorted_dict = {}
        self.line = line
        self.word_list = []
        self.occurrences_dict_to_sort = dict()
        self.occurrence_check = {}
        self.sector_id = 0
        self.checksum = ''
        self.__parse_data()
        self.is_room_real = False

    def __parse_data(self):
        all_words_in_line = self.line.split('-')
        only_words = all_words_in_line[:-1]
        self.checksum = all_words_in_line[-1].split("[")[1].strip(']')
        self.sector_id = all_words_in_line[-1].split("[")[0]
        self.word_list = only_words

    def number_of_occurrences_sorted(self) -> None:
        occurrences_dict = {q: 0 for q in string.ascii_lowercase[:26]}
        for word in self.word_list:
            for char in word:
                occurrences_dict[char] += 1
        alphabetic = {key: value for key, value in sorted(occurrences_dict.items())}
        sorted_dict = {key: value for key, value in sorted(alphabetic.items(), key=lambda x: x[1], reverse=True)}
        self.occurrences_sorted_dict = sorted_dict

    def calculate_checksum(self):
        checksum_list = []
        max_checksum = 0
        for i in self.occurrences_sorted_dict.keys():
            if self.occurrences_sorted_dict[i] > 0 and max_checksum < 5:
                checksum_list.append(i)
                max_checksum += 1
        checksum_calculated = ''.join(checksum_list)
        return checksum_calculated


if __name__ == "__main__":
    sector_sum = []
    encrypted_data_object = EncryptedData("test.txt") # zrobic funkcje sector_sum ktora zwraca, zeby nie zajmowac pamieci na pole
    for room_object in encrypted_data_object.lines_object_list:
        room_object.number_of_occurrences_sorted()
        checksum = room_object.calculate_checksum()
        is_room_real = (room_object.checksum == checksum)
        print('is room real: ', is_room_real)
        print('r.checksum: ', room_object.checksum)
        print('checksum: ', checksum)
        print('=======================================')
    print('sum of sector id for real rooms: ', sum(sector_sum))


