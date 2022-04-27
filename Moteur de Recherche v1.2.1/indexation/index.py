"""# Index"""
import re
import pandas as pd

stop_words = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off",
              "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]


def formate_word(words):
    res = []
    for tempWord in words.split(' '):
        tempWord = re.sub(r'[^a-zA-Z0-9]', '', tempWord)
        tempWord = tempWord.lower()
        tempWord = tempWord.strip()
        if tempWord not in stop_words:
            res.append(tempWord)
    return res


def get_index(data):
    """Get all informations in data to make a word index

    Args:
        data (_DataFrame_): _All the data got from the CSV File_

    Returns:
        _dict_: _Dict of Word and their Book id /position in title_
    """
    root = 'Title'
    data_index = dict()
    for i in range(len(data[root])):
        docId = data['Text#'][i]
        #words = data[root][i].split(' ')
        words = formate_word(data[root][i])
        for y, word in enumerate(words):
            if word not in data_index.keys():
                data_index[word] = dict()
            if docId not in data_index[word].keys():
                data_index[word][docId] = list()
            data_index[word][docId].append(y)
    print('--------------Index Created--------------')
    return data_index


def get_books_by_list_of_ids(data, ids: list()):
    """Get All book that matchs with the specific list of ids : ids

    Args:
        data (_DataFrame_): _The data we need to explore_
        ids (list): _List of ids to find in data_

    Returns:
        _DataFrame: _A smaller DataFrame with the ids we searched for_
    """
    books = dict()
    for key in data.keys():
        books[key] = list()

    for i in range(len(ids)):
        for key in data.keys():
            books[key].append(data.loc[data['Text#'] == ids[i]][key].values)
    res = pd.DataFrame(books)
    return res
