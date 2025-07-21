from rl_agent.planner import AdaptivePlanner
import numpy as np
from vision_monitoring.monitor import EnvironmentalMonitor
from nlp_engagement.sentiment_analysis import CitizenEngagement
from federated_learning.federated_model import FederatedClient


if __name__ == "__main__":
    planner = AdaptivePlanner()
    state = planner.get_state()
    action = planner.choose_action(state)
    planner.update_policy(state, action, reward=1.0)

    nlp = CitizenEngagement()
    feedback = "We need more green spaces and better waste management."
    print("Extracted keywords:", nlp.process_feedback(feedback))

    monitor = EnvironmentalMonitor()
    dummy_image = np.random.randint(0, 255, (100, 100), dtype=np.uint8)
    print("Environmental status:", monitor.analyze_image(dummy_image))

    client = FederatedClient(local_data=[1.2, 2.3, 3.1])
    client.send_update()
