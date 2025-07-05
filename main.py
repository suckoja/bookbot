import sys
from stats import get_num_words
from stats import get_character_frequency
from stats import sort_dictionaries

def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
    f.close()
    return file_contents
  
def report(book_path, num_words, frequencies):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for item in frequencies:
    print(f"{item[0]}: {item[1]}")
  print("============= END ===============")

def main():
  # Access command-line arguments
  if len(sys.argv) > 1:
    book_path = sys.argv[1]
  else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  # get book content
  content = get_book_text(book_path)

  # get the word count
  num_words = get_num_words(content)

  # get the dictionary of characters and their counts
  frequencies = get_character_frequency(content)

  # Report bookbot
  report(book_path, num_words, frequencies)

if __name__ == "__main__":
  main()