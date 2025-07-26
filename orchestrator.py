from agents import budget_expert, legal_expert, marketing_expert, critic_expert

def classify_query(query):
    tags = []
    if any(word in query.lower() for word in ["budget", "afford", "cost", "invest", "spend", "financial", "price", "pricing", "Q1", "Q2", "Q3", "Q4", "quarter", "ROI", "outsource", "in-house", "onboarding"]):
        tags.append("budget")
    if any(word in query.lower() for word in ["legal", "compliant", "gdpr", "regulation", "privacy", "data", "license"]):
        tags.append("legal")
    if any(word in query.lower() for word in ["launch", "market", "marketing", "audience", "position", "channel", "tagline", "social", "HR", "sales", "fintech", "onboarding"]):
        tags.append("marketing")
    return tags

def orchestrate(query):
    tags = classify_query(query)
    response = {"query": query, "summary": "", "budget": {}, "legal": {}, "marketing": {}, "critic": {}}

    if "budget" in tags:
        response["budget"] = budget_expert.respond(query)
    if "legal" in tags:
        response["legal"] = legal_expert.respond(query)
    if "marketing" in tags:
        response["marketing"] = marketing_expert.respond(query)

    summary = []
    if response["budget"]:
        summary.append(response["budget"].get("recommendation", ""))
    if response["legal"]:
        summary.append(response["legal"].get("recommendation", ""))
    if response["marketing"]:
        summary.append(response["marketing"].get("recommendation", ""))

    response["summary"] = " ".join(summary)
    response["critic"] = critic_expert.review_plan(response)

    return response