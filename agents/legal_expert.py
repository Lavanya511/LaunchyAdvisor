import random
    
def respond(query):
    if any(word in query.lower() for word in ["legal", "compliant", "gdpr", "regulation", "privacy", "data", "license"]):
        
        compliant = random.choice([True, False])
        issues = []

        legal_issues = [
            "Intellectual Disputes",
            "Law Violations",
            "Breach of Contract",
            "Regulatory Compliance Issues",
            "Data Privacy and Security Breaches"
        ]

        if not compliant:
            issues.append(random.choice(legal_issues))
        
        return {
            "Compliant": compliant,
            "Issues": issues,
            "Recommendation": "Proceed with legal compliance as planned." if compliant else "Address legal blockers before proceeding."
        }
    return {
        "Compliant": False,
        "Issues": ["Query not related to legal matters."],
        "Recommendation": "Not applicable."
    }
