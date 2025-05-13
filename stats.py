def get_num_words(book):
    return len(book.split())
    # Count the number of words in the book
    
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

def sort_dict_by_value(d):
    sorted_counts = sorted(d.items(), key=lambda item: item[1], reverse=True)
    return(sorted_counts) 
    # Sort the dictionary by value in descending order