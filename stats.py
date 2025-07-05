def get_num_words(content):
  words = content.split()
  return len(words)

def get_character_frequency(content):
  lowercase = content.lower()
  # prepare dictionary
  frequency = {}
  for c in set(lowercase):
    frequency[c] = lowercase.count(c)
  return sort_dictionaries(frequency)

def sort_on(item):
  return item[1]
  
def sort_dictionaries(dictionaries):
  sort_items = sorted(dictionaries.items())
  sort_items.sort(reverse=True, key=sort_on)
  return sort_items
