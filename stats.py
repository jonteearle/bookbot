def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    lower_case = text.lower()
    unique_chars = set()
    chars = {}
    for char in lower_case:
        if char not in unique_chars:
            unique_chars.add(char)
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def sort_on(items):
    return items["num"]

def sort_num_chars(dict):
    dict_list = []
    for char in dict:
        new_dict = {}
        new_dict["char"] = char
        new_dict["num"] = dict[char]
        dict_list.append(new_dict)
    sorted_list = dict_list.sort(reverse=True, key=sort_on)
    return dict_list