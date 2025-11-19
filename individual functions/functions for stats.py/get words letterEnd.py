
example = {
    'document1': ['that', 'when', 'the', 'powerbook', 'falls', 'asleep', 'he', 'said', 'he', 'was', 'sure', 'that',
                  'such', 'a', 'thing', 'existed', 'and'],
    'document2': ['freeware', 'somebody', 'in', 'was', 'also', 'having', 'trouble', 'using', 'a', 'spigot', 'in', 'his',   # this is how corpus_data will look like( this is fake corpus but it follows the same format)
                  'of', 'screenplay', 'which', 'fixed', 'things'],
    'document3': ['the', 'monitor', 'is', 'very', 'good', 'however', 'it', 'seems', 'that', 'the', 'does', 'not',
                  'support', 'vga', 'the', 'why', 'did', 'you', 'buy', 'it']
}


# Returns a list with all words in the corpus that end with a given letter
# the parameter data is a container to be used for such task
# the parameter letter is a string, indicating the letter
def get_words_letter_end(data, letter):
    print('get_word_letter_end: ' + letter + ': ', end='')
    words = []
    for document, list in data.items():     # if word[-1] in list in key in example is equal to letter, then append word to words.
        for word in list:
            if word[-1] == letter:
                words.append(word)
    return words


print(get_words_letter_end(example, 'r'))