from flask import request, Flask, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from collections import Counter
import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(50))
    urgency = db.Column(db.String(20))
    sentiment = db.Column(db.String(20))

@app.route('/api/topic_distribution')
def topic_distribution():
    topics = [f.topic for f in Feedback.query.all()]
    counts = Counter(topics)
    data = {
        "labels": list(counts.keys()),
        "datasets": [{
            "label": "Topics",
            "data": list(counts.values()),
            "backgroundColor": ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF"]
        }]
    }
    return jsonify(data)

@app.route('/api/urgency_levels')
def urgency_levels():
    urgencies = [f.urgency for f in Feedback.query.all()]
    counts = Counter(urgencies)
    data = {
        "labels": list(counts.keys()),
        "datasets": [{
            "label": "Urgency",
            "data": list(counts.values()),
            "backgroundColor": ["#28a745", "#ffc107", "#fd7e14", "#dc3545"]
        }]
    }
    return jsonify(data)

@app.route('/api/sentiment_analysis')
def sentiment_analysis():
    sentiments = [f.sentiment for f in Feedback.query.all()]
    counts = Counter(sentiments)
    data = {
        "labels": list(counts.keys()),
        "datasets": [{
            "label": "Sentiment",
            "data": list(counts.values()),
            "backgroundColor": ["#007bff", "#6c757d", "#dc3545"]
        }]
    }
    return jsonify(data)

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    topic = request.form['topic']
    urgency = request.form['urgency']
    sentiment = request.form['sentiment']

    new_feedback = Feedback(topic=topic, urgency=urgency, sentiment=sentiment)
    db.session.add(new_feedback)
    db.session.commit()

    return redirect('/')  # Redirect to dashboard or confirmation page


if __name__ == '__main__':
    app.run(debug=True)
