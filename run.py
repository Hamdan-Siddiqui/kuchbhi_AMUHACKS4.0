from flask import Flask, render_template, request
from psychologist import counselling

app = Flask(__name__)

text = ""
suggestion = ""

@app.route('/')
def home():
    return render_template("base.html")

@app.route('/submit', methods=["POST"])
def submit():
    try:
        text = request.form['text']
        suggestion = counselling(text)
        return render_template('base.html', suggestion = suggestion), suggestion
    except Exception as e:
        print(str(e))
        return str(e)

if __name__ == '__main__':
    app.run()