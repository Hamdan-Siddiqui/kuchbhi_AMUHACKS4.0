from flask import Flask, render_template, request, redirect, url_for
from psychologist import counselling

app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    return render_template("base.html")

@app.route('/process', methods=["GET"])
def processing_input():
    text = request.args.get('text')
    suggestion = "..."
    emotion = "..."
    
    if text:
        try:
            suggestion, emotion = counselling(text)
            print("Got it boss")
        except Exception as e:
            print(f"Error occurred: {e}")
            suggestion = f"Error: {e}"
    
    print(suggestion)
    return redirect(url_for("activities_page", suggestion=suggestion, emotion=emotion))

@app.route("/activities")
def activities_page():
    suggestion = request.args.get('suggestion')
    emotion = request.args.get('emotion')
    return render_template("happiness.html", suggestion=suggestion, emotion=emotion)

@app.route('/journaling')
def journaling():
    return render_template('journaling.html')

@app.route('/goal-setting')
def goal_setting():
    return render_template('goal_setting.html')

@app.route('/creativity')
def creativity():
    return render_template('creativity.html')

@app.route('/mindfulness')
def mindfulness():
    return render_template('mindfulness.html')

@app.route('/planning')
def planning():
    return render_template('planning.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/thought-journal')
def thought_journal():
    return render_template('thought_journal.html')

@app.route('/call-a-friend')
def call_a_friend():
    return render_template('call_a_friend.html')

@app.route('/signup', methods=["GET"])
def signup_page():
    email = request.args.get("email")
    password = request.args.get("password")
    print(email,password)
    return render_template("signup.html")

@app.route('/login', methods=["GET"])
def login_page():
    email = request.args.get("email")
    password = request.args.get("password")
    print(email,password)
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)