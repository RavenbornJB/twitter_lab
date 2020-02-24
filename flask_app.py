from flask import Flask, render_template, request
from twitter_mapper import user_analysis


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return user_analysis(user)
    return render_template('login.html')


if __name__ == "__main__":
    app.run()



# from flask import Flask, render_template, request, redirect, url_for
# from /home/RavenbornJB/twitter_mapper import user_analysis


# app = Flask(__name__)


# @app.route('/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         user = request.form['username']
#         user_analysis(user)
#         return redirect(url_for('mapper'))
#     return render_template('login.html')


# @app.route('/user_map')
# def mapper():
#     return render_template('index.html')


# if __name__ == "__main__":
#     app.run()