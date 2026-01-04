def get_count_of_words(book_contents):
    list_of_words = book_contents.split()
    return len(list_of_words)

def get_count_of_characters(text):
    character_count = {}
    for char in text.lower():
        character_count[char] = character_count.get(char,0) + 1
    return character_count

def sort_on(items):
    return items["num"]

def sort_character_count(character_dict):
    sorted_list = []
    for k,v in character_dict.items():
        dict_template = {"char":k, "num":v}
        sorted_list.append(dict_template)
    sorted_list.sort(reverse=True, key=sort_on)
    
    return sorted_list

