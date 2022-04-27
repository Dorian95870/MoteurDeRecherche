from indexation import get_books_by_list_of_ids
from ranking import get_sorted_books_by_score
import re
from flask import Flask, render_template, request, redirect
from waitress import serve


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result_page')
def result_page():
    user_request = request.args.get('q')
    app.config['request'] = user_request
    docs = get_sorted_books_by_score(
        app.config['dataSet'], app.config['myIndex'], app.config['request'])
    book_list = str(docs)
    book_list = re.sub(r'[^\w\s]', '', book_list)
    result_id = book_list.split(' ')
    try:
        result_id = [int(i) for i in result_id]
        found_books = get_books_by_list_of_ids(
            (app.config['dataSet']), result_id)
        found_books_titles = found_books['Title'].values
        found_books_authors = found_books['Authors'].values
        iterator = 0
        title_author_id_array = []
        for iterator in range(found_books['Title'].size):
            title_author_id_array.append(
                (found_books_titles[iterator], found_books_authors[iterator], result_id[iterator]))
        return render_template('results.html', titles_authors_id=title_author_id_array, length=len(title_author_id_array), request=app.config['request'])
    except ValueError:
        return render_template('NoResult.html', request=app.config['request'])


def start_server(index, data):
    app.config['myIndex'] = index
    app.config['dataSet'] = data
    print("Project Library is ON 🟢")
    print("Go to http://127.0.0.1:5000 to access the website")
    serve(app, host="127.0.0.1", port=5000)
    print("Project Library is OFF 🔴")

    # app.run(debug=False)
