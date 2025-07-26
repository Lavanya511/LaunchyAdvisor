def review_plan(response):
    feedback = []
    if response.get("budget", {}).get("Can afford") is False:
        feedback.append("Re-evaluate the financial plan or cut costs.")
    if response.get("legal", {}).get("Compliant") is False:
        feedback.append("Address legal blockers before proceeding.")
    if response.get("marketing", {}).get("Launch score") and response["marketing"]["Launch score"] < 7:
        feedback.append("Consider refining your marketing strategy to better reach your audience.")
    if not feedback:
        feedback.append("This is an excellent plan ✨. While a few optimizations might be beneficial, there are no significant concerns.")

    return {"feedback": feedback}