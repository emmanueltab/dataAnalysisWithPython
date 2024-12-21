# Returns the average length of the words in a document
# the parameter data is a container to be used for such task
# the parameter document is the name of the document (strindata = {
cheese =  {'document1': ['that', 'when', 'the', 'powerbook', 'falls', 'asleep', 'he', 'said', 'he', 'was', 'sure', 'that',
                    'such', 'a', 'thing', 'existed', 'and'],
        'document2': ['freeware', 'somebody', 'in', 'was', 'also', 'having', 'trouble', 'using', 'a', 'spigot', 'in', 'his',   # this is how corpus_data will look like( this is fake corpus but it follows the same format)
                    'of', 'screenplay', 'which', 'fixed', 'things'],
        'document3': ['the', 'monitor', 'is', 'very', 'good', 'however', 'it', 'seems', 'that', 'the', 'does', 'not',
                    'support', 'vga', 'the', 'why', 'did', 'you', 'buy', 'it'],
        'document4' : ['thee', 'thee']
    }

def avg_length(data, document):
    print('avg_length: ' + document + ': ',  end='')
    
    for docume in data:
        if document == docume:
            the_document = data.get(docume)
            
    average = 0
    total_words = len(the_document)
    total_letters = 0

    for word in the_document:
        total_letters = total_letters + len(word)

    average = total_letters / total_words
    return average

print(avg_length(cheese, 'document4'))



