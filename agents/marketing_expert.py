import random
from random import randint

def respond(query):
    if any(word in query.lower() for word in ["launch", "market", "marketing", "audience", "position", "channel", "tagline", "social", "HR", "sales", "fintech", "onboarding"]):
        
        channels = ["LinkedIn", "TechCrunch"]
        launch_score = randint(5, 10)
        
        return {
            "Launch score": launch_score,
            "Channel": random.choice(channels),
            "Recommendation": "This is a good marketing strategy." if launch_score > 7 else "Consider refining your marketing strategy to better reach your audience."
        }
    return {
        "Launch score": 0,
        "Channel": None,
        "Recommendation": "Query not marketing-related."
    }