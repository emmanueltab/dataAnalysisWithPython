# Build a dictionary where the key is a word and the value 
# is a list of all documents where that word appears

from pprint import pprint as pp
example = {
    'document1': ['that', 'when', 'the', 'powerbook', 'falls', 'asleep', 'he', 'said', 'he', 'was', 'sure', 'that',
                  'such', 'a', 'thing', 'existed', 'and'],
    'document2': ['freeware', 'somebody', 'in', 'was', 'also', 'having', 'trouble', 'using', 'a', 'spigot', 'in', 'his',   # this is how corpus_data will look like( this is fake corpus but it follows the same format)
                  'of', 'screenplay', 'which', 'fixed', 'things'],
    'document3': ['the', 'monitor', 'is', 'very', 'good', 'however', 'it', 'seems', 'that', 'the', 'does', 'not',
                  'support', 'vga', 'the', 'why', 'did', 'you', 'buy', 'it'],

    'document4' : ['the', 'tho', 'tho', 'the', 'asd', 'asd', 'fgjghjg', 'therolgoyt'] #  number of times word appears in document / 2 unique word
}



    # This is a dictionary where the
    # Key -> word in the corpus
    # Value -> list with names of all documents where that word appears

# Builds the doc_inverted_index dictionary by using another container as
# argument on the parameter data
def build_doc_inverted_index(data):

    temp_dictionary = {}
    # creates the "skeleton"of the dictionary
    for document, word_list in data.items():
        for word in word_list:
           temp_dictionary[word] = []
    
    for word, list in temp_dictionary.items():
        for document, list in data.items():
            if word in list:
                temp_dictionary[word].append(document)

    return temp_dictionary


pp(build_doc_inverted_index(example))
