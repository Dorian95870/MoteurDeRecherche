from flask import Flask, render_template, request, session, redirect
from filtering import filterByRequest

app = Flask(__name__)

@app.route('/')
def index():
    userRequest = request.args.get('q')
    if type(userRequest) != type(None):
        docs, count = filterByRequest(app.config['myIndex'], userRequest)
        app.config['results'] = count
        return redirect("/result")
    return render_template('index.html')

@app.route('/result')
def result():
    return str(app.config['results']) + " résultats !"

def startServer(index):
    app.config['myIndex'] = index
    app.run(debug=False)