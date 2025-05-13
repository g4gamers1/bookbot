import sys
import stats 
def main():
        book_path = get_path_to_book()
        book_text = get_book_text(book_path)
        num_words = stats.get_num_words(book_text)
        get_num_characters = stats.count_chars(book_text)
        sorted_dict = stats.sort_dict_by_value(get_num_characters)
        structure_text(book_path, num_words, sorted_dict)
        
        
    #stats.structure_text()

def get_path_to_book():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1] 

def get_book_text(path):
    with open(path) as f:
        return f.read()

def structure_text(book_path, num_words, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}..")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_dict:
        if not item[0].isalpha():
            continue
        print(f"{item[0]}: {item[1]}")
    print("============= END ===============")

         
main() 