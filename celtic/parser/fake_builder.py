# Don't modify this file, it provides some fake data, so that the student in charge of stats can test
# the code even if the dictionaries in parser are not completed. This also helps the student responsible
# for working on the parser module to understand what is the format of the expected output.

# This is a dictionary
# Key -> document name
# Value -> List of all words in that document
fake_corpus_data = {
    'document1': ['that', 'when', 'the', 'powerbook', 'falls', 'asleep', 'he', 'said', 'he', 'was', 'sure', 'that',
                  'such', 'a', 'thing', 'existed', 'and'],
    'document2': ['freeware', 'somebody', 'in', 'was', 'also', 'having', 'trouble', 'using', 'a', 'spigot', 'in', 'his',
                  'of', 'screenplay', 'which', 'fixed', 'things'],
    'document3': ['the', 'monitor', 'is', 'very', 'good', 'however', 'it', 'seems', 'that', 'the', 'does', 'not',
                  'support', 'vga', 'the', 'why', 'did', 'you', 'buy', 'it']
}

# This is a dictionary
# Key -> document name
# Value -> another dictionary, where:
#     Key -> word in document
#     Value -> number of times that word appears on that document
fake_doc_word_index = {
    'document1': {'that': 2,
                  'he': 2,
                  'when': 1,
                  'the': 1,
                  'powerbook': 1,
                  'falls': 1,
                  'asleep': 1,
                  'said': 1,
                  'was': 1,
                  'sure': 1,
                  'such': 1,
                  'a': 1,
                  'thing': 1,
                  'existed': 1,
                  'and': 1
                  },
    'document2': {'in': 2,
                  'freeware': 1,
                  'somebody': 1,
                  'was': 1,
                  'also': 1,
                  'having': 1,
                  'trouble': 1,
                  'using': 1,
                  'a': 1,
                  'spigot': 1,
                  'his': 1,
                  'of': 1,
                  'screenplay': 1,
                  'which': 1,
                  'fixed': 1,
                  'things': 1
                  },
    'document3': {'the': 3,
                  'it': 2,
                  'monitor': 1,
                  'is': 1,
                  'very': 1,
                  'good': 1,
                  'however': 1,
                  'seems': 1,
                  'that': 1,
                  'does': 1,
                  'not': 1,
                  'support': 1,
                  'vga': 1,
                  'why': 1,
                  'did': 1,
                  'you': 1,
                  'buy': 1
                  }

}

# This is a dictionary
# Key -> word in corpus
# Value -> the total number of times that word appears in the corpus
fake_global_count_index = {
    'the': 4,
    'that': 3,
    'he': 2,
    'was': 2,
    'a': 2,
    'in': 2,
    'it': 2,
    'when': 1,
    'powerbook': 1,
    'falls': 1,
    'asleep': 1,
    'said': 1,
    'sure': 1,
    'such': 1,
    'thing': 1,
    'existed': 1,
    'and': 1,
    'freeware': 1,
    'somebody': 1,
    'also': 1,
    'having': 1,
    'trouble': 1,
    'using': 1,
    'spigot': 1,
    'his': 1,
    'of': 1,
    'screenplay': 1,
    'which': 1,
    'fixed': 1,
    'things': 1,
    'monitor': 1,
    'is': 1,
    'very': 1,
    'good': 1,
    'however': 1,
    'seems': 1,
    'does': 1,
    'not': 1,
    'support': 1,
    'vga': 1,
    'why': 1,
    'did': 1,
    'you': 1,
    'buy': 1
}

# This is a dictionary
# Key -> document name
# Value -> another dictionary, where:
#     Key -> word in document
#     Value -> number of times that word appears on that document / total number of words in the document
fake_word_count_index = {
    'document1': {'that': 0.1176,
                  'he': 0.1176,
                  'when': 0.0588,
                  'the': 0.0588,
                  'powerbook': 0.0588,
                  'falls': 0.0588,
                  'asleep': 0.0588,
                  'said': 0.0588,
                  'was': 0.0588,
                  'sure': 0.0588,
                  'such': 0.0588,
                  'a': 0.0588,
                  'thing': 0.0588,
                  'existed': 0.0588,
                  'and': 0.0588
                  },
    'document2': {'in': 0.1052,
                  'freeware': 0.0526,
                  'somebody': 0.0526,
                  'was': 0.0526,
                  'also': 0.0526,
                  'having': 0.0526,
                  'trouble': 0.0526,
                  'using': 0.0526,
                  'a': 0.0526,
                  'spigot': 0.0526,
                  'his': 0.0526,
                  'of': 0.0526,
                  'screenplay': 0.0526,
                  'which': 0.0526,
                  'fixed': 0.0526,
                  'things': 0.0526
                  },
    'document3': {'the': 0.1500,
                  'it': 0.1000,
                  'monitor': 0.0500,
                  'is': 0.0500,
                  'very': 0.0500,
                  'good': 0.0500,
                  'however': 0.0500,
                  'seems': 0.0500,
                  'that': 0.0500,
                  'does': 0.0500,
                  'not': 0.0500,
                  'support': 0.0500,
                  'vga': 0.0500,
                  'why': 0.0500,
                  'did': 0.0500,
                  'you': 0.0500,
                  'buy': 0.0500
                  }

}

# This is a dictionary
# Key -> document name //STRING
# Value -> another dictionary, where: // INTEGER
#     Key -> word in document
#     Value -> number of times that word appears on that document / total number of unique words in that document
fake_weighted_word_count_index = {
    'document1': {'that': 0.1538,
                  'he': 0.1538,
                  'when': 0.0769,
                  'the': 0.0769,
                  'powerbook': 0.0769,
                  'falls': 0.0769,
                  'asleep': 0.0769,
                  'said': 0.0769,
                  'was': 0.0769,
                  'sure': 0.0769,
                  'such': 0.0769,
                  'a': 0.0769,
                  'thing': 0.0769,
                  'existed': 0.0769,
                  'and': 0.0769
                  },
    'document2': {'in': 0.1333,
                  'freeware': 0.0666,
                  'somebody': 0.0666,
                  'was': 0.0666,
                  'also': 0.0666,
                  'having': 0.0666,
                  'trouble': 0.0666,
                  'using': 0.0666,
                  'a': 0.0666,
                  'spigot': 0.0666,
                  'his': 0.0666,
                  'of': 0.0666,
                  'screenplay': 0.0666,
                  'which': 0.0666,
                  'fixed': 0.0666,
                  'things': 0.0666
                  },
    'document3': {'the': 0.2000,
                  'it': 0.1333,
                  'monitor': 0.0666,
                  'is': 0.0666,
                  'very': 0.0666,
                  'good': 0.0666,
                  'however': 0.0666,
                  'seems': 0.0666,
                  'that': 0.0666,
                  'does': 0.0666,
                  'not': 0.0666,
                  'support': 0.0666,
                  'vga': 0.0666,
                  'why': 0.0666,
                  'did': 0.0666,
                  'you': 0.0666,
                  'buy': 0.0666
                  }
}

# This is a dictionary
# Key -> word in the corpus
# Value -> list with names of all documents where that word appears
fake_doc_inverted_index = {
    'that': ['document1', 'document3'],
    'he': ['document1'],
    'the': ['document1', 'document3'],
    'powerbook': ['document1'],
    'somebody': ['document2']
}

# This is a dictionary
# Key -> document name
# Value -> list of unique words in document
fake_document_dictionary = {
    'document1': ['when', 'the', 'powerbook', 'falls', 'asleep', 'said', 'was', 'sure', 'such', 'a', 'thing', 'existed',
                  'and'],
    'document2': ['freeware', 'somebody', 'was', 'also', 'having', 'trouble', 'using', 'a', 'spigot', 'his', 'of',
                  'screenplay', 'which', 'fixed', 'things'],
    'document3': ['monitor', 'is', 'very', 'good', 'however', 'seems', 'that', 'does', 'not', 'support', 'vga', 'why',
                  'did', 'you', 'buy']
}

# This is a dictionary
# Key -> word in corpus,
# Value -> logarithm in base 10 of (total number of documents in corpus / number of documents containing that word)
fake_adjusted_index = {
    'the': 0.1760,      # log(3/2)
    'that': 0.1760,     # log(3/2)
    'he': 0.4771,       # log(3/1)
    'was': 0.4771,      # log(3/1)
    'a': 0.1760,        # log(3/1)
    'in': 0.1760,       # log(3/1)
    'it': 0.1760,       # log(3/1)
    'when': 0.4771,
    'powerbook': 0.4771,
    'falls': 0.4771,
    'asleep': 0.4771,
    'said': 0.4771,
    'sure': 0.4771,
    'such': 0.4771,
    'thing': 0.4771,
    'existed': 0.4771,
    'and': 0.4771,
    'freeware': 0.4771,
    'somebody': 0.4771,
    'also': 0.4771,
    'having': 0.4771,
    'trouble': 0.4771,
    'using': 0.4771,
    'spigot': 0.4771,
    'his': 0.4771,
    'of': 0.4771,
    'screenplay': 0.4771,
    'which': 0.4771,
    'fixed': 0.4771,
    'things': 0.4771,
    'monitor': 0.4771,
    'is': 0.4771,
    'very': 0.4771,
    'good': 0.4771,
    'however': 0.4771,
    'seems': 0.4771,
    'does': 0.4771,
    'not': 0.4771,
    'support': 0.4771,
    'vga': 0.4771,
    'why': 0.4771,
    'did': 0.4771,
    'you': 0.4771,
    'buy': 0.4771
}
