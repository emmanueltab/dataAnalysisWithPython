# Build a dictionary where the key is the name of the 
# document, and the value is another dictionary, where 
# the key is a word in that document and the value is a 
# number of how many times that word appears in that 
# document divided by the total number of words in that document
from pprint import pprint as pp
example =  {'document1': ['that', 'when', 'the', 'powerbook', 'falls', 'asleep', 'he', 'said', 'he', 'was', 'sure', 'that',
                    'such', 'a', 'thing', 'existed', 'and'],
        'document2': ['freeware', 'somebody', 'in', 'was', 'also', 'having', 'trouble', 'using', 'a', 'spigot', 'in', 'his',   # this is how corpus_data will look like( this is fake corpus but it follows the same format)
                    'of', 'screenplay', 'which', 'fixed', 'things'],
        'document3': ['the', 'monitor', 'is', 'very', 'good', 'however', 'it', 'seems', 'that', 'the', 'does', 'not',
                    'support', 'vga', 'the', 'why', 'did', 'you', 'buy', 'it']
    }

# This is a dictionary where the
# Key -> document name
# Value -> another dictionary, where:
#     Key -> word in document
#     Value -> number of times that word appears on that document / total number of words in the document


# Builds the word_count_index dictionary by using another container as
# argument on the parameter data
def build_word_count_index(data):  # build
    temp_dictionary = {}  # entire dictionary
    inner_dictonary = {}  # keys and values within document
    count_total_words = []  # List of the amount of unique words for each document
    go_up_per_document = 0  # Index for count total words for each individual document

    for document, word_list in data.items():
        count_total_words.append(len(word_list)) # appends the length of each word list from data to count total words

    for document, word_list in data.items(): # first nested loop, iterates each individual word in data
        for word in word_list:
            inner_dictonary[word] = word_list.count(word) / count_total_words[go_up_per_document]
        temp_dictionary[document] = inner_dictonary # creates a key (document) = value (inner_dictionary)
        inner_dictonary = {} # emptys inner_dictionary
        go_up_per_document = go_up_per_document + 1  # moves to next document N+1

    return temp_dictionary

pp(build_word_count_index(example))

