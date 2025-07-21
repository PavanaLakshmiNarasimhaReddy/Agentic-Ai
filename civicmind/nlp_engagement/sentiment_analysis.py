import re

class CitizenEngagement:
    def process_feedback(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        keywords = set(words)
        return keywords
