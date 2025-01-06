def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = split_string(text)
    return len(words)

def get_character_count(text):
    character_count = {}
    words = split_string(text)
    character_count_list = []
    for word in words:
        for character in word:
            #print(character)
            #input("wait")
            character = character.lower()
            if character not in character_count:
                character_count[character] = 0
            character_count[character] += 1
    for character in character_count:
        count = character_count[character]
        if character.isalpha():
            character_count_list.append({"character":character,"count":count})
        #print(character_count_list)
    return character_count_list

def split_string(text):
    splitted = text.split()
    #print(f"{splitted}")
    #input("Wait")
    return splitted

def sort_on(dict):
    #print(dict["count"])
    return dict["count"]

def main():    
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f'{num_words} words found in the document')
    character_count = get_character_count(text)
    #print(character_count)
    character_count.sort(reverse=True,key=sort_on)
    #print(character_count)
    for character in character_count:
        print(f'The \'{character["character"]}\' character was found \'{character["count"]}\' times')

main()