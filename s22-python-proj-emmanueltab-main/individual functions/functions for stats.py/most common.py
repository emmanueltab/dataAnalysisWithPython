# the number of times the most common word appears in the corpus, the parameter data is a container 
# to be useed for such task. most_common_word.py




example_list = {
    'document1': ['that', 'when', 'the', 'powerbook', 'falls', 'asleep', 'he', 'said', 'he', 'was', 'sure', 'that',
                  'such', 'a', 'thing', 'existed', 'and'],
    'document2': ['freeware', 'somebody', 'in', 'was', 'also', 'having', 'trouble', 'using', 'a', 'spigot', 'in', 'his',   # this is how corpus_data will look like( this is fake corpus but it follows the same format)
                  'of', 'screenplay', 'which', 'fixed', 'things'],
    'document3': ['the', 'monitor', 'is', 'very', 'good', 'however', 'it', 'seems', 'that', 'the', 'does', 'not',
                  'support', 'vga', 'the', 'why', 'did', 'you', 'buy', 'it']
}



# Returns the number of times the most common word appears in the corpus, the parameter
# data is a container to be used for such task
def most_common_word(data):
    print('most_common_word: ', end='')                 # create a for loop that will 
    word = ''                                           # create a list with all the words of the corpus(document1 + document2 + document3)
    count = 0
    counter = 0
    element_and_count = {}
    all_the_words = [] # this will have all the elements in the list
    for document, words in data.items():
        all_the_words = all_the_words + words # done
    
    for element in all_the_words:
        counter = all_the_words.count(element) # fills element_and_count 
        element_and_count[element] = counter

    word = max(element_and_count, key = element_and_count.get)  # gets the key with the largest value from element_and_count
    count = element_and_count.get(word)

    return(word, count)


    #for element in all_the_words:



   
        

    # return(word, count)
        

    #return (word, count)
print(most_common_word(example_list))
 
