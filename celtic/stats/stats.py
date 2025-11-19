"""stats functions

This module computes some statistics from the text corpus
"""


# Returns the number of times the most common word appears in the corpus, the parameter
# data is a container to be used for such task
def most_common_word(data):    
    print('most_common_word: ', end='')                 
    word = ''                                           
    count = 0
    counter = 0
    element_and_count = {}
    all_the_words = [] 
    for document, words in data.items():  # interates every list and adds them to all_the_words
        all_the_words = all_the_words + words 
    
    for element in all_the_words:
        counter = all_the_words.count(element) # iterates through every word in all_the_words and counts how many times that word repeats
        element_and_count[element] = counter  #  makes element a key and counter(how many times word repeats) as the value.

    word = max(element_and_count, key = element_and_count.get)  # gets the key with the largest value from element_and_count
    count = element_and_count.get(word)  # gets the value of word which is the word that repeats the most and assigns it to count
    
    return (word, count)

# source that I used for max(line 23):
# https://tinyurl.com/3bhvubfb

def avg_length(data, document):
    print('avg_length: ' + document + ': ',  end='')
    
    for docume in data:
        if document == docume:
            the_document = data.get(docume)   # if docuement(the positonal parameter) is the same as docume then the document will be the
        else:                                       # value of docume
            pass 
            
    average = 0
    total_words = len(the_document)   # it is then used over here 
    total_letters = 0

    for word in the_document:
        total_letters = total_letters + len(word)  # iterates through each word in the_docuement and adds the length of it to total_letters

    average = total_letters / total_words    # does average
    return average



# Returns the document with the highest number of words
# If the second parameter is not given (the default)
# returns the document with the highest number of unique words
# data is a container to be used for such task
def get_largest_document(data, unique=False): # assuming data will be in a tuple or list (all the words in each document will be in a list/ tuple)
    print('get_largest_document: ', end='')
    document = ''
    all_sizes = {}
    all_unique = {}
    
    get_largest_document = ''
    doc_with_most_unique_words = ''
    comparer2 = 0
    comparer = 0

    if unique == False:  # will return the document with the most words is unique is false
        for documen, list in data.items():  # creates a dictonary with the docuements being the keys and the size of their words being the value
            all_sizes[documen] = len(list)

        comparer = all_sizes[documen]

        for document, number in all_sizes.items():  # compares each document
            if number > comparer:
                comparer = number
                get_largest_document = document

        return get_largest_document    # returns largest document
     
    else:
        for document in data:
            all_unique[document] = 0

        

        for document, list in data.items():              # if the count of each word is 1 then 1 gets added to the value of each value
             for word in list:
                 if list.count(word) == 1:
                     all_unique[document] = all_unique[document] + 1

        comparer2 = all_unique[document]
        for document, num in all_unique.items():  # finds the one with the most unique words
             if num > comparer2:
                comparer2 = num
                doc_with_most_unique_words = document
        return doc_with_most_unique_words

# Returns a list with all words in the corpus that end with a given letter
# the parameter data is a container to be used for such task
# the parameter letter is a string, indicating the letter
def get_words_letter_end(data, letter):
    print('get_word_letter_end: ' + letter + ': ', end='')
    words = []

    for document, list in data.items():     
        for word in list:
            if word[-1] == letter:    # iterates through every individual word in data
                words.append(word)    # if word[-1] in list in key in example is equal to letter, then append word to words.
    return words



# Returns a list with all words in the corpus that begin with a given letter
# the parameter data is a container to be used for such task
# the parameter letter is a string, indicating the letter

def get_words_letter_begin(data, letter):
    print('get_word_letter_begin: ' + letter + ': ', end='')
    words = []
    for doc, listt in data.items():     
        for word in listt:              # iteraetes through each word from data
            if word[0] == letter:    # if word[0] is the same as  letter, then itll be appended it to words.
                words.append(word)
        
    return(words)



# Returns a list with all words in the corpus of a given size
# the parameter data is a container to be used for such task
# the parameter size is an integer, indicating the size
def get_words_size(data, size):
    print('get_word_size: ' + str(size) + ': ', end='')
    words = []      # the list that will have the words that of the same size of size(the 2nd postional parameter)

    for document, list in data.items():
        for word in list:      # this iterates through each word in the corpus
            if len(word) == size:   
                words.append(word)    # if the len(word) is equal to size(2nd postional parameter) then it will put that word in word

    return words


# computes the average size of words in the corpus
# the parameter data is a container to be used for such task
def compute_avg(data):
    print('compute_avg: ', end='')
    total_letters = 0
    total_words = 0
    average = 0

    for document, words in data.items():   
        total_words = total_words + len(words)   # iterates through each word_list in data and adds the length to total_words
        for word in words:
            total_letters = len(word) + total_letters # iterates through each individual word in data and adds the length to total_letters

    average = total_letters / total_words 
    return average


# Returns a list with all words in the corpus whose size is greater than
# the corpus words average size
# Returns a list with all words in the corpus whose size is greater than
# the corpus words average size
def get_words_grater_avg(data, avg_size):    # avg_size will be the function compute_avg when it is called. 
    print('get_words_grater_avg: ', end='')      
    words = []  # list with all the words that are greater than avg_size

    for docu, list in data.items():          
        for wordd in list:           # iterates through each individual word. if it is greater than avg_size then itll get appended ot words
            if len(wordd) > avg_size:   
                words.append(wordd)
    return words
    

