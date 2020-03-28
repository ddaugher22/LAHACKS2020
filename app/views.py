from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/im_bored')
def im_bored():
 	return render_template('im_bored.html', title='Im Bored')

@app.route('/at_home')
def at_home():
 	return render_template('at_home.html', title='At Home')

@app.route('/outdoors')
def outdoors():
 	return render_template('outdoors.html', title='Outdoors')

@app.route('/chat')
def chat():
 	return render_template('chat.html', title='Chat')

@app.route('/video_call')
def video_call():
 	return render_template('video_call.html', title='Video Call')

