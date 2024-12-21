
example = {
    'document1': ['that', 'when', 'the', 'powerbook', 'falls', 'asleep', 'he', 'said', 'he', 'was', 'sure', 'that',
                  'such', 'a', 'thing', 'existed', 'and'],
    'document2': ['freeware', 'somebody', 'in', 'was', 'also', 'having', 'trouble', 'using', 'a', 'spigot', 'in', 'his',   # this is how corpus_data will look like( this is fake corpus but it follows the same format)
                  'of', 'screenplay', 'which', 'fixed', 'things'],
    'document3': ['the', 'monitor', 'is', 'very', 'good', 'however', 'it', 'seems', 'that', 'the', 'does', 'not',
                  'support', 'vga', 'the', 'why', 'did', 'you', 'buy', 'it']
}

# Returns a list with all words in the corpus of a given size
# the parameter data is a container to be used for such task
# the parameter size is an integer, indicating the size
def get_words_size(data, size):
    print('get_word_size: ' + str(size) + ': ', end='')
    words = []
    for document, list in data.items():
        for word in list:
            if len(word) == size:  # if len(word) in list in key in data is the same value as size, append word to words. 
                words.append(word)
    return words


print(get_words_size(example, 3))