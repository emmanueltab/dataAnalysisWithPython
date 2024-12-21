# Build a dictionary where the key is a word in the corpus 
# and the value is computed as logarithm in base 10 of
# (total number of documents in corpus / number of 
# documents containing that word)




from pprint import pprint as pp
import math
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
# Key -> word in corpus,
# Value -> logarithm in base 10 of (total number of documents in corpus / number of documents containing that word)
adjusted_index = {}


def build_adjusted_index(data):
    temp_dictionary = {}
    total_number_documents = 0
    for document in data:   
        total_number_documents = total_number_documents + 1

    for document, word_list in data.items():  
        for word in word_list:
           temp_dictionary[word] = 0
    
    for word, list in temp_dictionary.items():
        for document, list in data.items():
            if word in list:
                temp_dictionary[word] = temp_dictionary[word] + 1
        temp_dictionary[word] = math.log((total_number_documents / temp_dictionary[word]), 10) # this is the same as log10(total/word)

    return temp_dictionary



print(build_adjusted_index(example))