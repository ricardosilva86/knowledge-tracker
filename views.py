from app import app, db
from models import MainTopic, Topic, SubTopic
from flask import render_template

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/add/maintopic', methods=['GET'])
def add_maintopic():
    return render_template('add_maintopic.html')

@app.route('/add/topic', methods=['GET'])
def add_topic():
    return render_template('add_topic.html')

@app.route('/add/subtopic', methods=['GET'])
def add_subtopic():
    return render_template('add_subtopic.html')

@app.route('/show/progress', methods=['GET'])
def show_progress():
    maintopics = db.session.query(MainTopic).join(Topic).join(SubTopic)
    topics = db.session.query(Topic).all()
    subtopics = db.session.query(SubTopic).all()
    return render_template('show_progress.html', maintopics=maintopics, topics=topics, subtopics=subtopics)