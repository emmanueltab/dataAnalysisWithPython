""""builder functions

This module has functions for populating dictionaries from different containers
"""

import celtic.parser as pa
import math

# *************************************************
# Dictionaries for storing data from the text files.
# *************************************************

# This is a dictionary where the
# Key -> document name
# Value -> List of all words in that document
corpus_data = {}  # corpus_data{Key : Value} //'string' : ['str1','str2', ...'strX']

# This is a dictionary where the
# Key -> document name
# Value -> another dictionary, where:
#     Key -> word in document
#     Value -> number of times that word appears on that document
doc_word_index = {}  # nested dictionary -> doc_word_index = {Key : Value} //{'string' : integer}

# This is a dictionary where the
# Key -> word in corpus
# Value -> the total number of times that word appears in the corpus
global_count_index = {}

# This is a dictionary where the
# Key -> document name
# Value -> another dictionary, where:
#     Key -> word in document
#     Value -> number of times that word appears on that document / total number of words in the document
word_count_index = {}

# This is a dictionary where the
# Key -> document name
# Value -> another dictionary, where:
#     Key -> word in document
#     Value -> number of times that word appears on that document / total number of unique words in that document
weighted_word_count_index = {}

# This is a dictionary where the
# Key -> word in the corpus
# Value -> list with names of all documents where that word appears
doc_inverted_index = {}

# This is a dictionary where the
# Key -> document name
# Value -> list of unique words in document
doc_dictionary = {}

# This is a dictionary where the
# Key -> word in corpus,
# Value -> logarithm in base 10 of (total number of documents in corpus / number of documents containing that word)
adjusted_index = {}

# *************************************************
# Functions
# *************************************************
# Builds the doc_word_index dictionary by using another container as
# argument on the parameter data
# Don't modify this function
def build_doc_word_index(data):
    temp_dictionary = {}
    for document, words_list in data.items():
        inner_dictionary = {}

        for word in words_list:
            if word in inner_dictionary:
                # if value exist it increments by 1
                inner_dictionary[word] += 1
            else:
                # if dictionary does not exist, it will create a dictionary and value of 1
                inner_dictionary[word] = 1

        temp_dictionary[document] = inner_dictionary

    return temp_dictionary

# Builds the global_count_index dictionary by using another container as
# argument on the parameter data
# Don't modify this function
def build_global_count_index(data):
    temp_dictionary = {}
    for document,words_list in data.items():
        for word in words_list:
            if word in temp_dictionary:
                temp_dictionary[word] += 1
            else:
                temp_dictionary[word] = 1
    return temp_dictionary

# This is a dictionary where the
# Key -> document name
# Value -> another dictionary, where:
#     Key -> word in document
#     Value -> number of times that word appears on that document
# doc_word_index = {}  # nested dictionary -> doc_word_index = {Key : Value} //{'string' : integer}
# Builds the word_count_index dictionary by using another container as
# argument on the parameter data
### Description:
#1a: Build a dictionary where the key is the name of the document,
#1b: and the value is another dictionary, where the key is a word in that document
#1c: and the value is a number of how many times that word appears in that document divided by the total number of words in that document.
def build_word_count_index(data):  # build
    temp_dictionary = {} # entire dictionary
    inner_dictonary = {} # keys and values within document
    count_total_words = [] # List of the amount of unique words for each document
    go_up_per_document = 0 # Index for count total words for each individual document

    for document, word_list in data.items():
        count_total_words.append(len(word_list)) # appends the length of each word list from data to count total words

    for document, word_list in data.items(): # first nested loop, iterates each individual word in data
        for word in word_list:
            inner_dictonary[word] = word_list.count(word) / count_total_words[go_up_per_document]
        temp_dictionary[document] = inner_dictonary # creates a key (document) = value (inner_dictionary)
        inner_dictonary = {} # emptys inner_dictionary
        go_up_per_document = go_up_per_document + 1 # moves to next document N+1

    return temp_dictionary

# Builds the weighted_word_count_index dictionary by using another container as
# argument on the parameter data
## Teamate helped with this function **********************************
def build_weighted_word_count_index(data): # build
    main_dictonary = {} # whole dictionary that the function creates
    inner_dictonary = {}
    temp_dictionary = {}
    all_unique = {}
    count_unique = 0
    all_unique_list = []
    count_all_unique_list = 0
    for document, word_list in data.items():
        for word in word_list:
            # iterates through each individual word in data. if the count of that word is 1
            if word_list.count(word) == 1:
                count_unique = count_unique + 1   # then it adds 1 to count_unique and puts count_unique as the value for each document in all_unique
        all_unique[document] = count_unique
        count_unique = 0  # in summary it creates a dictonary with all the documents and the amount of unique words in each document

    for document, unique in all_unique.items(): # appends every value(count_unique) from all_unique to all_unique_list
        all_unique_list.append(unique)

    for document, word_list in data.items():
        for word in word_list:   # iterates over each individual word in data
            # creates inner dictonary which is the dictionary with the key being each word and the value being the-
            inner_dictonary[word] = word_list.count(word) / all_unique_list[count_all_unique_list]  # count of the word/ the unique words in its document
            # with key being word in document and value being number of times that word repeats
        main_dictonary[document] = inner_dictonary  # creates main dictonary with the documents being the keys and the inner_dictonary from abouve being the value
        inner_dictonary = {}
        count_all_unique_list = count_all_unique_list + 1  # it then resets inner dictonary so it can be used again and adds 1 to count_all-unique_list 
                                                            # so it can iterate through each total unique words from all_unique_list
    temp_dictionary = main_dictonary

    return temp_dictionary   # assings main_dictonary to temp_dictionary because I wanst sure if it would cause errors if it didnt return temp_dictionary

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
                temp_dictionary[word].append(document) # adds value for word within the list
    return temp_dictionary
# Builds the doc_dictionary dictionary by using another container as
# argument on the parameter data
### Pulling data from test-2.py, Lines 41:42
# using the same first nested loop from build_weighted_word_count_index
## pulls unique words in value amount from each document
def build_doc_dictionary(data):
    temp_dictionary = {}
    all_unique = {}  # dictionary
    count_unique = 0 # value
    temp_dictionary = {}

    for document, word_list in data.items():
        for word in word_list:
            # creates all_values with key being document and value being amount of unique words in the document
            if word_list.count(word) == 1:
                count_unique = count_unique + 1
        all_unique[document] = count_unique # document //key && count_unique // value
        count_unique = 0

    temp_dictionary = all_unique
    return temp_dictionary


# Builds the adjusted_index dictionary by using another container as
# argument on the parameter data
def build_adjusted_index(data):
    temp_dictionary = {}
    total_number_documents = 0
    for document in data:   
        total_number_documents = total_number_documents + 1  # adds to total_number_documents for every key in data

    for document, word_list in data.items():    # creates the "skeleton for temp dictionary"
        for word in word_list:
           temp_dictionary[word] = 0
# teamate assisted with second nested for loop
    for word, list in temp_dictionary.items():
        for document, list in data.items():    
            if word in list:     # if word(key) is in list from data then it will run the buttom code
                temp_dictionary[word] = temp_dictionary[word] + 1       # adds one to the value of each key with word being the key
        temp_dictionary[word] = math.log((total_number_documents / temp_dictionary[word]), 10) # I used the math module for this.
                                                                                        # this is the same as log10(total/value for word)
    return temp_dictionary


