# computes the average size of words in the corpus
# the parameter data is a container to be used for such task
example = {
    'document1': ['that', 'when', 'the', 'powerbook', 'falls', 'asleep', 'he', 'said', 'he', 'was', 'sure', 'that',
                  'such', 'a', 'thing', 'existed', 'and'],
    'document2': ['freeware', 'somebody', 'in', 'was', 'also', 'having', 'trouble', 'using', 'a', 'spigot', 'in', 'his',   # this is how corpus_data will look like( this is fake corpus but it follows the same format)
                  'of', 'screenplay', 'which', 'fixed', 'things'],
    'document3': ['the', 'monitor', 'is', 'very', 'good', 'however', 'it', 'seems', 'that', 'the', 'does', 'not',
                  'support', 'vga', 'the', 'why', 'did', 'you', 'buy', 'it']
}

def compute_avg(data):
    print('compute_avg: ', end='')
    total_letters = 0
    total_words = 0
    average = 0
    for document, words in data.items():   # gets total amount of words for entire corpus and adds them to total_words
        total_words = total_words + len(words)
        for word in words:
            total_letters = len(word) + total_letters # gets total amount of letters in the entire corpus and adds them to total_letters

    average = total_letters / total_words
    
    return average


# Returns a list with all words in the corpus whose size is greater than
# the corpus words average size
def get_words_grater_avg(data, avg_size):
    print('get_words_grater_avg: ', end='')
    words = []
    for docu, list in data.items():          # this code will call the function that computes total average
        for wordd in list:
            if len(wordd) > avg_size:   # if word in each list in each key is greater than avg_size (in arguement), then it will append word to words.
                words.append(wordd)
    return words
    
    
print(get_words_grater_avg(example, compute_avg(example)))  # calls average. this isnt needed but its cool and I like it not being hard coded.