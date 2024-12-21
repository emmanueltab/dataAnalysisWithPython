# Emmanuel will use this one
from turtle import *
import celtic as cs
import celtic.stats as stats
import celtic.parser as parser
import celtic.viz as viz
import pprint

# to see a help for this package type help('celtic') in the python interpreter
# This is the main test script for Student A

def main():
    print('***************************************************')
    print('building dictionaries')
    print('***************************************************')
    print('I am student A emmanuel...')

    # builds a dictionary with documents and words in each document
    parser.corpus_data = cs.parser.read_file('fake_corpus.txt')
    pprint.pprint(parser.corpus_data)

    # using the dictionary parser.corpus_data built in the previous step
    # builds a new dictionary and stores it in the variable parser.doc_word_index
    # Note: as you build the other dictionaries, look at the output of the
    # ones previously build to decide with is the best suited to be passed as
    # argument to each function. In this example, parser.corpus_data is used
    # but most likely you have to use a different one.
    parser.doc_word_index = parser.build_doc_word_index(parser.corpus_data)
    pprint.pprint(parser.doc_word_index)

    parser.global_count_index = cs.parser.build_global_count_index(parser.corpus_data)
    pprint.pprint(parser.global_count_index)

    parser.word_count_index = cs.parser.build_word_count_index(parser.corpus_data)
    pprint.pprint(parser.word_count_index)

    parser.weighted_word_count_index = cs.parser.build_weighted_word_count_index(parser.corpus_data)
    pprint.pprint(parser.weighted_word_count_index)

    parser.doc_inverted_index = cs.parser.build_doc_inverted_index(parser.corpus_data)
    pprint.pprint(parser.doc_inverted_index)

    parser.doc_dictionary = cs.parser.build_doc_dictionary(parser.corpus_data)
    pprint.pprint(parser.doc_dictionary)

    parser.adjusted_index = cs.parser.build_adjusted_index(parser.corpus_data)
    pprint.pprint(parser.adjusted_index)

    print('***************************************************')
    print('computing stats')
    print('***************************************************')

    # You have to implement the functions in stats, then depending on what
    # dictionaries you built before, you have to decide which one to pass as
    # argument to these stats functions.
    print(stats.most_common_word(parser.corpus_data))
    print(stats.get_largest_document(parser.corpus_data))
    print(stats.avg_length(parser.corpus_data, 'document1'))
    print(stats.get_words_letter_end(parser.corpus_data, 'p'))
    print(stats.get_words_letter_begin(parser.corpus_data, 'n'))
    print(stats.get_words_size(parser.corpus_data, 4))   # the average is hard coded. I might try using compute_avg instead of 4
    compute_av = stats.compute_avg(parser.corpus_data)
    print(compute_av)
    print(stats.get_words_grater_avg(parser.corpus_data, compute_av))

    print('***************************************************')
    print('vizualization')
    print('***************************************************')

    # plots a bar chart defined in celtic.viz
    viz.plot_top_k_freq_words_doc(parser.doc_word_index, 'document2', 5)
    viz.plot_bottom_k_freq_words_doc(parser.doc_word_index, 'document3', 3)
    viz.plot_freq_word_doc(parser.corpus_data, ['document1', 'document2'], "the")

    # makes the the plot stop, comment this line when working on your code
    #viz.render()

main()
