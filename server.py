from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "Password"

@app.route("/")
def index():
    if not 'count' in session:
        session['count'] = 0
    session['count'] += 1
    return render_template('index.html', click_count = session['count'])

@app.route("/plus_one")
def plus_one():
    return redirect ("/")

@app.route("/plus_two")
def plus_two():
    session['count'] += 1
    return redirect ("/")

@app.route("/reset")
def reset():
    session['count'] = 0
    return redirect("/")

@app.route("/destroy_session")
def destroy_session():
    session.clear()
    session['count'] = 0
    return redirect("/")

@app.route("/increment", methods=['POST'])
def increment():
    print(request.form['increment_amount'])
    session['count'] += int(request.form['increment_amount']) - 1
    return redirect ("/")

if __name__=="__main__":
    app.run(debug=True)