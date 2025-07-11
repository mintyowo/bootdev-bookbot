def get_num_words(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
        file_length = file_contents.split()
        print("----------- Word Count ----------")
        print(f"Found {len(file_length)} total words")
def get_num_letters(path_to_file):
    cool_dict = {}

    with open(path_to_file) as file:
        file_contents = file.read()
        for letter in file_contents.lower():
            if letter in cool_dict:
                cool_dict[letter] += 1
            else: 
                cool_dict[letter] = 1
    return cool_dict   
def sort_key(items):
    return items["num"]
def sort_letters(letters):
    cool_list = []
    for key,value in letters.items():
        cool_list.append({"char": key,"num": value})
    cool_list.sort(reverse=True, key=sort_key)   
    print("--------- Character Count -------")
    for wowdict in cool_list:
        if wowdict["char"].isalpha() == False:
            pass
        else:
            hi_guys = wowdict["char"]
            hows_it_going = wowdict["num"]
            print(f"{hi_guys}: {hows_it_going}")
    print("============= END ===============")
