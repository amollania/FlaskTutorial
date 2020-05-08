from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Home
@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    today = 'To day is...'
    return render_template('index.html', todayHtml = today)

# About
@app.route('/about')
def about():
    return 'About Page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Try again'
        else:
            return redirect(url_for('profile'))
    return render_template('login.html', error =error)

@app.route('/profile')
def secret():
    return render_template('profile.html')

if __name__ == "__main__":
    app.run()