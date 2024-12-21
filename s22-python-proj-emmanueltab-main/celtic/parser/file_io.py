import celtic.parser as parser

# reads from a text file and returns a dictionary where the key is the name of
# a document and the value is a list with all words in that document
def read_file(file):
    list_of_words = []
    documents = {}
    doc_title = ''

    print('input file is: ' + file)

    with open('texts/input/' + file, encoding='utf-8') as f:
        count = 0
        for line in f:
            # remove some punctuation characters from the input line
            line = line.replace('\n','').replace('\'','').replace('"','').replace('(','').replace(')','')
            line = line.replace('?','').replace('!','').replace('.','').replace(',','').replace(';','').replace(':','')
            if line[:15] == 'corpus document':
                list_of_words = []
                doc_title = line[7:]
                documents[doc_title] = list_of_words
            else:
                # splits a a line from the file on the space character and returns
                # a list, where each element is a word from the line, removes empty
                # strings
                list_of_words += list(line.split(' '))
                list_of_words = [item for item in list_of_words if item != '']

                count += 1

            documents[doc_title] = list_of_words

    return documents
