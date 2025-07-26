import random  

def respond(query):
    if any(word in query.lower() for word in ["budget", "afford", "cost", "invest", "spend", "financial", "price", "pricing", "Q1", "Q2", "Q3", "Q4", "quarter", "ROI", "outsource", "in-house", "onboarding"]):
        
        estimated_cost = random.randint(5000, 20000)
        budget_remaining = random.randint(10000, 50000)
        if budget_remaining >= estimated_cost:
            can_afford = True
        else:
            can_afford = False
            
        recommendation = "You can proceed with this plan."
        
        return {
            "Can afford": can_afford,
            "Estimated cost": estimated_cost,
            "Budget remaining": budget_remaining,
            "Recommendation": recommendation if can_afford else "Re-evaluate the financial plan or cut costs."
        }
    return {
        "Can afford": False,
        "Estimated cost": None,
        "Budget remaining": None,
        "Recommendation": "Query not related to budget matters."
    }
    
