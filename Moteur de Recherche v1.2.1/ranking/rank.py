from indexation import get_books_by_list_of_ids
from filtering import filter_by_request
from enum import Enum
from datetime import datetime


class rankValues(Enum):
    AND = 10
    OR = 5
    DATE = 2

# classer en premier pour les documents qui contient plus de mots dans la requete


def ranking_by_and_or(dataIndex, request: str):
    """_ranking of the results by and fisrt and then by or_

    Args:
        dataIndex (_dict_): _the dataIndex we are using of or website_
        request (str): _the user request_

    Returns:
        _List_: _List of results with AND results first and Or after_
    """

    l3 = list()
    list_or, list_and = filter_by_request(dataIndex, request)
    l3.extend(list_and)
    l3.extend(list_or)

    # enveler les doublons
    list_of_ids = list()
    for i in l3:
        if i not in list_of_ids:
            list_of_ids.append(i)

    return list_or, list_and, list_of_ids


def _sort_ascending_by_score(res):
    return list(dict(sorted(res.items(), key=lambda item: item[1])).keys())


def get_sorted_books_by_score(data, dataIndex, request: str):
    """_Assigns a score to each document, this score defines the relevance of the document_

    Args:
        data (_dict_): _the data we are using of or website_
        dataIndex (_dict_): _the dataIndex we are using of or website_
        request (str): _the user request_

    Returns:
        _List_: _List of documents sort in descending order according to the score_
    """

    list_or, list_and, list_of_ids = ranking_by_and_or(dataIndex, request)

    # vvvvvv Scoring vvvvvv
    res = dict.fromkeys(list_of_ids, 0)
    docs_infos = get_books_by_list_of_ids(data, list_of_ids)

    # Score par type de filtrage
    for doc in list_or:
        res[doc] = rankValues.OR.value
    for doc in list_and:
        res[doc] = rankValues.AND.value

    for i, doc in enumerate(list_of_ids):
        temp_doc = docs_infos.loc[docs_infos['Text#'] == doc]

        # Score par date
        if datetime.strptime(temp_doc['Issued'][i][0], '%Y-%m-%d') >= datetime.strptime('2013-01-01', '%Y-%m-%d'):
            res[doc] += rankValues.DATE.value

        # Score par download count
        try:
            res[doc] += int((temp_doc['download_count'] /
                             data['download_count'].max())*20)
        except:
            res[doc] += 0

    res_sorted = _sort_ascending_by_score(res)

    return res_sorted[::-1]
