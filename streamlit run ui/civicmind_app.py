import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt

# Define agent personasst
agents = {
    "PoliticianBot": "As a politician, I believe in pragmatic policies that balance economic growth with public welfare.",
    "CitizenBot": "As a citizen, I care about how policies affect my daily life, my family, and my community.",
    "ActivistBot": "As an activist, I advocate for justice, sustainability, and long-term societal impact."
}

# Function to simulate agent response
def generate_response(agent_intro, topic, round_num):
    return f"{agent_intro} Regarding '{topic}', in round {round_num}, I think we should consider multiple perspectives to make informed decisions."

# Function to perform sentiment analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Streamlit UI
st.set_page_config(page_title="CivicMind Debate Simulator", layout="wide")
st.title("CivicMind Agentic AI Debate Simulator")

# Sidebar configuration
st.sidebar.header("Debate Configuration")
topic = st.sidebar.text_input("Enter Debate Topic", value="Climate Change Policy")
num_rounds = st.sidebar.slider("Number of Debate Rounds", min_value=1, max_value=10, value=5)

# Initialize session state
if "sentiment_history" not in st.session_state:
    st.session_state.sentiment_history = {agent: [] for agent in agents}

 # Run debate simulation
st.subheader(f"Debate Topic: {topic}")
for round_num in range(1, num_rounds + 1):
    st.markdown(f"### Round {round_num}")
    for agent_name, agent_intro in agents.items():
        response = generate_response(agent_intro, topic, round_num)
        sentiment = analyze_sentiment(response)
        st.session_state.sentiment_history[agent_name].append(sentiment)
        st.markdown(f"**{agent_name}**: {response}")
        st.markdown(f"_Sentiment Score_: `{sentiment:.2f}`")

# Plot sentiment trends
st.subheader("Sentiment Trend Over Rounds")
fig, ax = plt.subplots()
for agent_name, sentiments in st.session_state.sentiment_history.items():
    ax.plot(range(1, len(sentiments) + 1), sentiments, label=agent_name)
ax.set_xlabel("Round")
ax.set_ylabel("Sentiment Score")
ax.set_title("Sentiment Analysis Over Debate Rounds")
ax.legend()
st.pyplot(fig)
