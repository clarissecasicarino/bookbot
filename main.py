def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    length_of_words = count_words(text)
    counted_letters = count_letters(text)
    print(f"Letters: {counted_letters}")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
   splitted_text = text.split()
   return len(splitted_text)

def count_letters(characters):
    letter_counts = {}
    
    for char in characters:
        
        char = char.lower()
        
        # Checks if character is within the alphabet (a-z)
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    
    return letter_counts
            
    
main()
    