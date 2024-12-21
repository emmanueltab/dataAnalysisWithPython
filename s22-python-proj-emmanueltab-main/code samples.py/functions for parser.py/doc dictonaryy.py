# Build a dictionary where the key is the document name 
# and the value is a list of all unique words in that 
# document

example =  {'document1': ['that', 'when', 'the', 'powerbook', 'falls', 'asleep', 'he', 'said', 'he', 'was', 'sure', 'that',
                    'such', 'a', 'thing', 'existed', 'and'],
        'document2': ['freeware', 'somebody', 'in', 'was', 'also', 'having', 'trouble', 'using', 'a', 'spigot', 'in', 'his',   # this is how corpus_data will look like( this is fake corpus but it follows the same format)
                    'of', 'screenplay', 'which', 'fixed', 'things'],
        'document3': ['the', 'monitor', 'is', 'very', 'good', 'however', 'it', 'seems', 'that', 'the', 'does', 'not',
                    'support', 'vga', 'the', 'why', 'did', 'you', 'buy', 'it'],
    }


# Builds the doc_dictionary dictionary by using another container as
# argument on the parameter data
def build_doc_dictionary(data):
    all_unique = {}
    count_unique = 0
    temp_dictionary = {}
    for document, word_list in data.items():
        for word in word_list:
            # creates all_values with key being document and value being amount of unique words in the document
            if word_list.count(word) == 1:
                count_unique = count_unique + 1
        all_unique[document] = count_unique
        count_unique = 0

    temp_dictionary = all_unique 
    return temp_dictionary


print(build_doc_dictionary(example))

