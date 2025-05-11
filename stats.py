def get_book_as_string():
    num_words = 0
    with open("books/frankenstein.txt") as f:
        for line in f:
            line.split()
            for word in line.split():
                num_words += 1
        print(f"Found {num_words} total words")
    


def count_chars(text):
    char_counts = {}
    for char in text:
        # Convert to lowercase
        lower_char = char.lower()
        # Check if character exists in dictionary
        if lower_char in char_counts:
            char_counts[lower_char] += 1
        else:
            char_counts[lower_char] = 1
    return char_counts

def get_num_characters_each_time():
    with open("books/frankenstein.txt") as f:
        text = f.read()
    return count_chars(text)

def sort_dict_by_value():
    d = get_num_characters_each_time()
    # Sort the dictionary by value in descending order
    sorted_counts = sorted(d.items(), key=lambda item: item[1], reverse=True)
    return(sorted_counts) 

def sorted_dict_to_spaced_prints(sorted_dict):
    for char, count in sorted_dict:
        if char == "\n":
            print("\\n:", count)
        else:
            print(f"{char}: {count}")
    


def structure_text():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_book_as_string()
    print("--------- Character Count -------")
    sorted_dict_to_spaced_prints(sort_dict_by_value())
    print("============= END ===============")