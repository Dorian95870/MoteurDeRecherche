import re, requests
from indexation import *
from flask import Flask, render_template, request, session, redirect
from filtering import filterByRequest


app = Flask(__name__)

@app.route('/')
def index():
    userRequest = request.args.get('q')
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
def result_page():
    bookList = str(app.config['listOfBooks'])
    bookList = re.sub(r'[^\w\s]', '', bookList)
    result = bookList.split(' ')
    res ='['
    for x in result:
        url = requests.get("https://gutendex.com/books/" + x + "/")
        text = url.text
        res = res + text
        res = res + ','
    res = res + ']'
    res2 = res.split(',')
    return render_template('results.html',message =res2)

@app.route('/result_page2')
def result_page2():
    bookList = str(app.config['listOfBooks'])
    bookList = re.sub(r'[^\w\s]', '', bookList)
    result = bookList.split(' ')
    result = [int(i) for i in result]
    res = getBooksByListOfIds((app.config['dataSet']), result)
    return render_template('results.html',message = res)


def startServer(index, data):
    app.config['myIndex'] = index
    app.config['dataSet'] = data
    app.run(debug=False)