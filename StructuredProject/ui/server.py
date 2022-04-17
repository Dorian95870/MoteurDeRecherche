import re
from indexation import *
from flask import Flask, render_template, request, redirect
from filtering import filterByRequest


app = Flask(__name__)

@app.route('/')
def index():
    userRequest = request.args.get('q')
    app.config['request'] = userRequest
    if type(userRequest) != type(None):
        docsOR, docsAND = filterByRequest(app.config['myIndex'], userRequest)
        app.config['nbResults'] = len(docsOR)
        app.config['listOfBooks'] = docsOR
        return redirect("/result_page")
    return render_template('index.html')

@app.route('/result')
def result():
    BooksList = ""
    for x in range(len(app.config['listOfBooks'])):
        val = app.config['listOfBooks'][x]
        pyval = val.item()
        BooksList = BooksList + str(pyval) + '\n'
    
    return str(app.config['nbResults']) + " résultats ! " + BooksList


@app.route('/result_page')
def result_page2():
    bookList = str(app.config['listOfBooks'])
    bookList = re.sub(r'[^\w\s]', '', bookList)
    resultId = bookList.split(' ')
    try :
        resultId = [int(i) for i in resultId]
        foundBooks = getBooksByListOfIds((app.config['dataSet']), resultId)
        foundBooksTitles = foundBooks['Title'].values
        foundBooksAuthors = foundBooks['Authors'].values
        iterator = 0
        TitleAuthorIdArray = []
        for iterator in range (foundBooks['Title'].size) :
            TitleAuthorIdArray.append((foundBooksTitles[iterator],foundBooksAuthors[iterator],resultId[iterator]))
        return render_template('results.html',titlesAuthorsId = TitleAuthorIdArray, request = app.config['request'])
    except ValueError :
        return render_template('NoResult.html', request = app.config['request'])
    


def startServer(index, data):
    app.config['myIndex'] = index
    app.config['dataSet'] = data
    app.run(debug=False)