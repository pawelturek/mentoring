import string


class EncryptedData:


    def __init__(self, file_txt: str):
        with open(file_txt, "r") as f:
            while True:
                return [line.strip() for line in f.readlines()]


def count_letters2(code: str):
    word_list = []
    one_word: int = code.find('-')
    word_list.append(code[0:one_word])
    while True:
        second_word = code.find('-', one_word + 1, len(code))
        if any(char.isdigit() for char in code[one_word + 1:second_word]):
            second_word = code.find('[', one_word + 1, len(code))
            sector_id = code[one_word + 1:second_word]
            one_word = second_word
            second_word = code.find(']', one_word + 1, len(code))
            checksum = code[one_word + 1:second_word]
            break
        word_list.append(code[one_word + 1:second_word])
        one_word = second_word
    return word_list, sector_id, checksum


def number_of_occurrences(word_list: list):
    occurrences_dict = dict()
    for q in string.ascii_lowercase[:26]:
        occurrences_dict[q] = 0
    for w in word_list:
        for i in w:
            occurrences_dict[i] = occurrences_dict[i] + 1
    return occurrences_dict


def occurrences_sort(occurrences_dict: dict):
    alphabetic = {key: value for key, value in sorted(occurrences_dict.items())}
    sorted_dict = {key: value for key, value in sorted(alphabetic.items(), key=lambda x: x[1], reverse=True)}
    return sorted_dict


def calculate_checksum(occurrence_check: dict):
    checksum_list = []
    max_checksum = 0
    for i in occurrence_check.keys():
        if occurrence_check[i] > 0 and max_checksum < 5:
            checksum_list.append(i)
            max_checksum += 1
    checksum = ''.join(checksum_list)
    return checksum



def is_room_real(checksum_calculated: str, current_checksum: str, sector_id: int) -> int:
    if current_checksum == checksum_calculated:
        return int(sector_id)
    else:
        return 0


def main():
    total_sum = 0
    for line in range(0,len(open_file("test.txt"))):
        print('Is room real: ', is_room_real(calculate_checksum(occurrences_sort(number_of_occurrences(count_letters2(open_file("test.txt")[line])[0]))), count_letters2(open_file("test.txt")[line])[2], count_letters2(open_file("test.txt")[line])[1]))
        total_sum += is_room_real(calculate_checksum(occurrences_sort(number_of_occurrences(count_letters2(open_file("test.txt")[line])[0]))), count_letters2(open_file("test.txt")[line])[2], count_letters2(open_file("test.txt")[line])[1])
    return total_sum

print('suma sector id', main())




# print('count_letters2: ',count_letters2(open_file("test.txt")[0])[0]) #numer liniijki w pliku, 0 - word list, 1 - sector, 2 checksum, nr slowa
# print('number_of_occurrences: ',number_of_occurrences(count_letters2(open_file("test.txt")[0])[0][0]))
# print('aaaaaaaaaa')
# print(occurrences_sort(number_of_occurrences(count_letters2(open_file("test.txt")[0])[0])))
# print('number_of_occurrences: ',number_of_occurrences(count_letters2(open_file("test.txt")[0])[0]))
# print('sorted: ',occurrences_sort(number_of_occurrences(count_letters2(open_file("test.txt")[0])[0])))
# print(calculate_checksum(occurrences_sort(number_of_occurrences(count_letters2(open_file("test.txt")[0])[0]))))

#print('czek: ',count_letters2(open_file("test.txt")[0])[1])