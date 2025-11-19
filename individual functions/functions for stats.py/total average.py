# computes the average size of words in the corpus
# the parameter data is a container to be used for such task

data = {
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
    for document, words in data.items():   # gets total amount of words for entire corpus
        total_words = total_words + len(words)
        for word in words:
            total_letters = len(word) + total_letters

    average = total_letters / total_words
    return average, total_words, total_letters

print(compute_avg(data))



    
    




    