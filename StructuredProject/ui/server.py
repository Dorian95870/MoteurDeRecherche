import imp
from pydoc import doc
import numpy as np
from flask import Flask, render_template, request, session, redirect , jsonify
from filtering import filterByRequest

app = Flask(__name__)

@app.route('/')
def index():
    userRequest = request.args.get('q')
    if type(userRequest) != type(None):
        docs, count = filterByRequest(app.config['myIndex'], userRequest)
        app.config['results'] = count
        app.config['listOfBooks'] = docs
        return redirect("/result")
    return render_template('index.html')

@app.route('/result')
def result():
    BooksList = ""
    for x in range(len(app.config['listOfBooks'])):
        #print(app.config['listOfBooks'][x])
        val = app.config['listOfBooks'][x]
        pyval = val.item()
        BooksList = BooksList + str(pyval) + '\n'
    
    print('\n')
    print(BooksList)
    return str(app.config['results']) + " résultats ! " + BooksList
    

def startServer(index):
    app.config['myIndex'] = index
    app.run(debug=False)