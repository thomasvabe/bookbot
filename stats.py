def count_words(text):
    words = text.split()
    return len(words)

def get_characters(text):
    char_dict = {}
    for character in text:
        char = character.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def report(dictionary):
    report_list = []
    for char, count in dictionary.items():
        char_dict = {"char": char, "num": count}
        report_list.append(char_dict)

    def sort_on(dict_item):
        return dict_item["num"]
    
    report_list.sort(reverse=True, key=sort_on)

    return report_list
