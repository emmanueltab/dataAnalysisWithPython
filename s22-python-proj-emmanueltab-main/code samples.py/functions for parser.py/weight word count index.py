#  Build a dictionary where the key is the name of the 
# document, and the value is another dictionary, where 
# the key is a word in that document and the value is a 
# number of how many times that word appears in that 
# document divided by the number of unique words in 
# that document.
import pprint
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
# Key -> document name
# Value -> another dictionary, where:
#     Key -> word in document
#     Value -> number of times that word appears on that document / total number of unique words in that document
weighted_word_count_index = {}

def build_weighted_word_count_index(data): # build
    main_dictonary = {}
    inner_dictonary = {}
    temp_dictionary = {}
    all_unique = {}
    count_unique = 0
    all_unique_list = []
    count_all_unique_list = 0

    for document, word_list in data.items():
        for word in word_list:
            # creates all_values with key being document and value being amount of unique words in the document
            if word_list.count(word) == 1:
                count_unique = count_unique + 1
        all_unique[document] = count_unique    
        count_unique = 0

    for document, unique in all_unique.items():
        all_unique_list.append(unique)


    for document, word_list in data.items():
        for word in word_list:
            # builds main_dictonary with key being document, value being another dictionary
            inner_dictonary[word] = word_list.count(word) / all_unique_list[count_all_unique_list]
            # with key being word in document and value being number of times that word repeats
        main_dictonary[document] = inner_dictonary
        inner_dictonary = {}
        count_all_unique_list = count_all_unique_list + 1
    

    
    temp_dictionary = main_dictonary


    return temp_dictionary

    
  
            
pprint.pprint(build_weighted_word_count_index(example))

