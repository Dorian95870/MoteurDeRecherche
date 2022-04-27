"""# Filter"""
from indexation import formate_word


def _get_res_or(dataIndex, words):
    """Filter the list with OR

    Returns:
        _List_: _List result of OR filter_
    """
    docs_or = list()
    for i in range(len(words)):
        try:
            docs_or += dataIndex[words[i]]
        except:
            print('Aucun résulats pour la requete: {}'.format(words[i]))
    return docs_or


def _intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def _get_res_and(dataIndex, words):
    """Filter the list with AND

    Returns:
        _List_: _List result of AND filter_
    """
    docs_and = list()
    for i in range(len(words)):
        try:
            docs_and.append(dataIndex[words[i]])
        except:
            print('Aucun résulats pour la requete: {}'.format(words[i]))

    res = list()
    for i in range(len(docs_and)-1):
        res = _intersection(docs_and[i], docs_and[i+1])

    return res


def _format_request(request):
    request = re.sub(r'[^\w\s]', '', request)
    request = request.lower().split(' ')
    return


def filter_by_request(dataIndex, request: str):
    """Filter function : search all files in dataIndex that match with the request

    Args:
        dataIndex (_DataFrame_): _The dataIndex created witch contains all file word in a index_
        request (str): _The user request_

    Returns:
        _(List,List)_: _2 List one is the result of getresOR and the other is the result of getResAND_
    """
    # Definir nos règles de Filtrage

    # words_without_ponctuation = re.sub(r'[^\w\s]', '', request)
    # words = words_without_ponctuation.lower().split(' ')
    words = formate_word(request)

    return (_get_res_or(dataIndex, words), _get_res_and(dataIndex, words))
