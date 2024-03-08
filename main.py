def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    length_of_words = count_words(text)
    counted_letters = count_letters(text)
    printed_report = print_report(counted_letters, length_of_words)    
    
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


def print_report(counted_letters, word_count):
    # Convert dictionary to list of dictionaries
    letter_list = [{'letter': k, 'count': v} for k, v in counted_letters.items()]
    
    # Sort the list by the number of occurrences using the provided sort method
    letter_list.sort(reverse=True, key=lambda x: x['count'])
    
    # Printing the report
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for item in letter_list:
        print(f"The '{item['letter']}' character was found {item['count']} times")
    print(f"--- End report ---")       
    
main()
    