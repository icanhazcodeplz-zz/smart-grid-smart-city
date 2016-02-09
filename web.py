import os
from flask import Flask, render_template, request, redirect
# from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/[YOUR_DATABASE_NAME]'
# db = SQLAlchemy(app)

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('homepage.html')
    else:
        han_item = request.form['han_item']
        if han_item == 'dishwasher':
            return redirect('/dishwasher')
        elif han_item == 'dryer':
            return redirect('/dryer')


@app.route('/dishwasher')
def dishwasher():
    return render_template('10014678_Dishwasher.html')


@app.route('/dryer')
def dryer():
    return render_template('10050432_Dryer.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(debug=False)

