import os.path
import string

sector_sum = []
class EncryptedData:
    """loading encrypted data from txt file"""

    def __init__(self, file_txt: str):
        self.lines_object_list = []
        self.file_txt = file_txt
        self.local_dir = r'C:\Users\turekp\Desktop\mentoring\mentoring'
        self.file_path = os.path.join(self.local_dir, self.file_txt)
        print(self.file_path)

        try:
            with open(self.file_path, "r") as f:
                for line in f.readlines():
                    r = Room(line.strip())
                    self.lines_object_list.append(r)
        except IOError:
            raise IOError("{} not found in {}".format(self.file_txt, self.local_dir))



class Room:


    def __init__(self, line: str):
        self.occurrences_dict = {q: 0 for q in string.ascii_lowercase[:26]}
        self.line = line
        self.word_list = []
        self.checksum_calculated = ''
        self.current_checksum = ''
        self.checksum_calc = ''
        self.occurrences_dict_to_sort = dict()
        self.occurrence_check = {}
        self.sector_id = 0
        self.checksum = ''
        self.__parse_data()


    def __parse_data(self):
        one_word: int = self.line.find('-')
        self.word_list.append(self.line[0:one_word])
        while True:
            second_word = self.line.find('-', one_word+1, len(self.line))
            if any(char.isdigit() for char in self.line[one_word + 1:second_word]):
                second_word = self.line.find('[', one_word + 1, len(self.line))
                self.sector_id = int(self.line[one_word + 1:second_word])
                one_word = second_word
                second_word = self.line.find(']', one_word + 1, len(self.line))
                self.checksum = self.line[one_word + 1:second_word]
                break
            self.word_list.append(self.line[one_word + 1:second_word])
            one_word = second_word

 #   def __str__(self):
 #       return "word list: "+ str(self.word_list)+" sector id: "+ self.sector_id + " checksum :"\
 #               + self.checksum

    def number_of_occurrences(self, word_list: list):
        # occurrences_dict = dict()
        self.occurrences_dict = {q: 0 for q in string.ascii_lowercase[:26]}
        for w in word_list:
             for i in w:
                self.occurrences_dict[i] = self.occurrences_dict[i] + 1
        return self.occurrences_dict

    def occurrences_sort(self, occurrences_dict_to_sort: dict):
        self.occurrences_dict_to_sort = occurrences_dict_to_sort
        alphabetic = {key: value for key, value in sorted(self.occurrences_dict_to_sort.items())}
        sorted_dict = {key: value for key, value in sorted(alphabetic.items(), key=lambda x: x[1], reverse=True)}
        return sorted_dict

    def calculate_checksum(self, occurrence_check: dict):
        self.occurrence_check = occurrence_check
        checksum_list = []
        max_checksum = 0
        for i in self.occurrence_check.keys():
            if self.occurrence_check[i] > 0 and max_checksum < 5:
                checksum_list.append(i)
                max_checksum += 1
        self.checksum_calculated = ''.join(checksum_list)
        return self.checksum_calculated

    def is_room_real(self, checksum_calc: str, current_checksum: str, sector_id: int) -> int:
        self.checksum_calc = checksum_calc
        self.current_checksum = current_checksum
        self.sector_id = sector_id
        global sector_sum
        if self.current_checksum == self.checksum_calc:
            sector_sum.append(int(sector_id))
            return int(sector_id)
        else:
            return 0


def main():
    e = EncryptedData("test.txt")
    for r in e.lines_object_list:

        r.calculate_checksum(r.occurrences_sort(r.number_of_occurrences(r.word_list)))
        print(r.is_room_real(r.checksum_calculated, r.checksum, r.sector_id))
    print('sum of sector id for real rooms: ', sum(sector_sum))


main()