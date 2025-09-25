# python
def get_num_words(filepath: str) -> int:
    count = 0
    with open(filepath) as f:
        for line in f:
            count += len(line.split())
    return count

def get_char_count(filepath: str) -> dict[str, int]:
    char_count_dict = {}
    with open(filepath) as f:
        for line in f:
            strip_line = line.strip("\n").lower()
            for char in strip_line:
                if char in char_count_dict:
                    char_count_dict[char] += 1
                else:
                    char_count_dict[char] = 1
    return char_count_dict

def get_num(d):
    return d["num"]

def sorted_dict(raw_dict: dict) -> list:
    unsorted_list = []
    for key, value in raw_dict.items():
        if key.isalpha():
            unsorted_list.append({"char": key , "num": value})
    sorted_list = sorted(unsorted_list, key=get_num, reverse=True )
    return sorted_list
            