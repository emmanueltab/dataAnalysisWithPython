example_list = {
    'document1': ['that', 'when', 'the', 'powerbook', 'falls', 'asleep', 'he', 'said', 'he', 'was', 'sure', 'that',
                  'such', 'a', 'thing', 'existed', 'and'],

    'document2': ['freeware', 'somebody', 'in', 'was', 'also', 'having', 'trouble', 'using', 'a', 'a', 'spigot', 'in', 'his',   # this is how corpus_data will look like( this is fake corpus but it follows the same format)
                  'of', 'screenplay', 'which', 'fixed', 'things'],

    'document3': ['the', 'monitor', 'is', 'very', 'good', 'however', 'it', 'seems', 'that', 'the', 'does', 'not',
                  'support', 'vga', 'the', 'why', 'did', 'you', 'buy', 'it'],
    
    'document4' : ['good', 'farts'] # 2 unique
}



# Returns the document with the highest number of words
# If the second parameter is not given (the default)
# returns the document with the highest number of unique words
# data is a container to be used for such task
def get_largest_document(data, unique=False): # assuming data will be in a tuple or list (all the words in each document will be in a list/ tuple)
    print('get_largest_document: ', end='')
    document = ''
    all_sizes = {}
    all_unique = {}
    comparer = 0
    get_largest_document = ''
    doc_with_most_unique_words = ''
    comparer2 = 0
    if unique == False:  # will return the document with the most words is unique is false
        for documen, list in data.items():  # creates a dictonary with the docuements being the keys and the size of their words being the value
            all_sizes[documen] = len(list)

        comparer = all_sizes[documen]

        for document, number in all_sizes.items():
            if number > comparer:
                comparer = number
                get_largest_document = document

        return get_largest_document    # returns largest document
     
    else:
        for document in data:
            all_unique[document] = 0

        

        for document, list in data.items():
             for word in list:
                 if list.count(word) == 1:
                     all_unique[document] = all_unique[document] + 1

        comparer2 = all_unique[document]
        for document, num in all_unique.items():  # finds the one with the most unique words
             if num > comparer2:
                comparer2 = num
                doc_with_most_unique_words = document

        return doc_with_most_unique_words, all_unique

        


                    
print(get_largest_document(example_list, True))