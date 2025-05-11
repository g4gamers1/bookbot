
import stats  
def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        print(file_content)


    

def main():
    stats.structure_text()

main()