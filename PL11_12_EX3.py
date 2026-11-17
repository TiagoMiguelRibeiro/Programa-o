def sort_by_length(words):
    sorted_words = sorted(words, key=len)
    return sorted_words

sorted_words = sort_by_length(["apple", "pie", "banana", "kiwi"]) 
print(sorted_words)  # Output: ['pie', 'date', 'apple', 'banana', 'kiwi']
