from flask import Flask, request, redirect, url_for, \
     render_template, flash

from model import *

DEBUG = True
SECRET_KEY = 'hello_world'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def show_entries():
    data = BlogPost.select()
    return render_template('show_entries.html', data=data)


@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        entry = BlogPost(title = request.form['title'], text = request.form['description'])
        entry.save()
        flash('New entry was successfully posted')
        return redirect(url_for('show_entries'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run()
