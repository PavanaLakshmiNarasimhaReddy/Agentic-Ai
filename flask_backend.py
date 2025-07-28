
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from collections import Counter

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    topic = db.Column(db.String(100))
    urgency = db.Column(db.String(50))
    sentiment = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

def analyze_feedback(message):
    message_lower = message.lower()
    topic = "General"
    urgency = "Low"
    sentiment = "Neutral"

    if "road" in message_lower or "traffic" in message_lower:
        topic = "Infrastructure"
    elif "school" in message_lower or "education" in message_lower:
        topic = "Education"
    elif "hospital" in message_lower or "health" in message_lower:
        topic = "Healthcare"

    if "urgent" in message_lower or "immediately" in message_lower:
        urgency = "High"
    elif "soon" in message_lower or "important" in message_lower:
        urgency = "Medium"

    if "good" in message_lower or "happy" in message_lower or "great" in message_lower:
        sentiment = "Positive"
    elif "bad" in message_lower or "angry" in message_lower or "poor" in message_lower:
        sentiment = "Negative"

    return topic, urgency, sentiment

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    message = data.get('message', '')
    topic, urgency, sentiment = analyze_feedback(message)

    feedback = Feedback(message=message, topic=topic, urgency=urgency, sentiment=sentiment)
    db.session.add(feedback)
    db.session.commit()

    return jsonify({'status': 'success', 'topic': topic, 'urgency': urgency, 'sentiment': sentiment})

@app.route('/get_dashboard_data', methods=['GET'])
def get_dashboard_data():
    feedbacks = Feedback.query.all()
    topics = [fb.topic for fb in feedbacks]
    urgencies = [fb.urgency for fb in feedbacks]
    sentiments = [fb.sentiment for fb in feedbacks]

    topic_counts = dict(Counter(topics))
    urgency_counts = dict(Counter(urgencies))
    sentiment_counts = dict(Counter(sentiments))

    return jsonify({
        'topics': topic_counts,
        'urgencies': urgency_counts,
        'sentiments': sentiment_counts
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
