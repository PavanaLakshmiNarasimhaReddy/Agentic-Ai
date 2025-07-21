class FederatedClient:
    def __init__(self, local_data):
        self.local_data = local_data

    def train_local_model(self):
        return sum(self.local_data) / len(self.local_data)

    def send_update(self):
        update = self.train_local_model()
        print(f"Sending model update: {update}")
        return update
