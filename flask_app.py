from flask import Flask, render_template, request, redirect, url_for
from twitter_mapper import user_analysis


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        try:
            return user_analysis(user)
        except:
            return redirect(url_for('login'))
    return render_template('login.html')


if __name__ == "__main__":
    app.run()
