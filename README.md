# dataAnalysisWithPython 
Spring 2022 Intro to Programming Term Project

This was the project that a Joseph Barrera, and I worked on for "intro to programming" freshmen year at the University of St. Thomas.
Our professor was Dr. Carlos Monroy, professor of Computer Science at UST.

# Explaination:
In the celtic package there are 2 modules, parser and stats. 
We wrote the functions within those modules. Then in the main.py files, the functions will be called with the variable, parser.parser_data as the argument. parser.parser_data is a dictonary which will be filled by io_file.py, 

# io_file.py
a script that reads from a text file and returns a dictionary where the key is the name of
a document and the value is a list with all words in that document

# example: 
we will use as the example document to test our functions (it has the same format as parser_data):

example_list = {
    'document1': ['that', 'when', 'the', 'powerbook', 'falls', 'asleep', 'he', 'said', 'he', 'was', 'sure', 'that',
                'such', 'a', 'thing', 'existed', 'and'],
    'document2': ['freeware', 'somebody', 'in', 'was', 'also', 'having', 'trouble', 'using', 'a', 'spigot', 'in', 'his',   # this is how corpus_data will look like( this is fake corpus but it follows the same format)
                'of', 'screenplay', 'which', 'fixed', 'things'],
    'document3': ['the', 'monitor', 'is', 'very', 'good', 'however', 'it', 'seems', 'that', 'the', 'does', 'not',
                'support', 'vga', 'the', 'why', 'did', 'you', 'buy', 'it']
}