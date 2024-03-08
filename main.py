def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    length_of_words = count_words(text)
    print(f"Length of Words: {length_of_words}")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
   splitted_text = text.split()
   return len(splitted_text)
    
main()
    