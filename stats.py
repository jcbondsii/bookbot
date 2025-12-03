def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_letters(dictionary):
    dict = []
    for k, v in dictionary.items():
        dict.append({"letter": k, "num": v})
    return dict

def sort_on(items):
    return items["num"]