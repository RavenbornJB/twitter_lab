from flask import Flask, render_template, request, redirect, url_for
from twitter_mapper import user_analysis


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        if not user:
            return redirect(url_for('login'))
        return user_analysis(user)
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug = True)
