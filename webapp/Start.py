from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    userRequest = request.args.get('q')
    print(userRequest)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

