from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/im_bored')
def im_bored():
 	return render_template('im_bored.html', title='Im Bored')