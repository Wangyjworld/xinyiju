from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing
from flask import send_from_directory

app = Flask(__name__)





@app.route('/index')
@app.route('/')
def show_index():
    return render_template('index.html', title="house")

@app.route('/contact')
def show_contact():
    return render_template('contact.html', title="house")


@app.route('/about')
def show_about():
    return render_template('about.html', title="house")


@app.route('/features')
def show_features():
    return render_template('features.html', title="house")


@app.route('/work')
def show_work():
    return render_template('work.html', title="house")



@app.errorhandler(404)
def page_not_found():
    return render_template('404.html', title="house")


@app.errorhandler(500)
def page_not_found():
    return render_template('500.html', title="house")










if __name__ == '__main__':
    app.run()
