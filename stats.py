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