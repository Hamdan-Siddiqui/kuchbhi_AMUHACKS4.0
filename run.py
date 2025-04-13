from flask import Flask, render_template, request
from psychologist import counselling

app = Flask(__name__)

text = ""
suggestion = ""
@app.route('/', methods=["GET"])
def home():
    text = request.args.get('text')
    if text:
        try:
            suggestion = counselling(text)
            return render_template("base.html", suggestion=suggestion)
        except Exception as e:
            print(str(e))
            return str(e)
    return render_template("base.html")


if __name__ == '__main__':
    app.run()