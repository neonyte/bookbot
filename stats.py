def word_count(text):
    return text.split()

def char_count(text):
    lower_text = text.lower()
    letter_list = {
    }
    for char in lower_text:
        if char in letter_list:
            letter_list[char] = letter_list[char]+1
        else:
            letter_list[char] = 1
    return letter_list

def sort_char_count(dict):
    sorted_list = []
    for entry in dict:
        if entry.isalpha():
            temp_dict = {
                "char": entry, "num": dict[entry]
            }
            sorted_list.append(temp_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(items):
    return items["num"]