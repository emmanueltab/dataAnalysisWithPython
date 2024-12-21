example = {
    'document1': ['that', 'when', 'the', 'powerbook', 'falls', 'asleep', 'he', 'said', 'he', 'was', 'sure', 'that',
                  'such', 'a', 'thing', 'existed', 'and'],
    'document2': ['freeware', 'somebody', 'in', 'was', 'also', 'having', 'trouble', 'using', 'a', 'spigot', 'in', 'his',   # this is how corpus_data will look like( this is fake corpus but it follows the same format)
                  'of', 'screenplay', 'which', 'fixed', 'things'],
    'document3': ['the', 'monitor', 'is', 'very', 'good', 'however', 'it', 'seems', 'that', 'the', 'does', 'not',
                  'support', 'vga', 'the', 'why', 'did', 'you', 'buy', 'it'],

    'document4' : ['doggy', 'turtle', 'mary', 'john']
}

# Returns a list with all words in the corpus that begin with a given letter
# the parameter data is a container to be used for such task
# the parameter letter is a string, indicating the letter

def get_words_letter_begin(data, letter):
    print('get_word_letter_begin: ' + letter + ': ', end='')
    words = []
    for doc, listt in data.items():     # if word[0] in a list in a key in data is greater than letter, then it will append word to words.
        for word in listt:
            if word[0] == letter:
                words.append(word)
        
    return(words)

print(get_words_letter_begin(example, 'h'))