import json
from orchestrator import orchestrate

with open("promptsInterview.json") as f:
    prompts = json.load(f)

results = []
for item in prompts:
    result = orchestrate(item["query"])
    results.append(result)

with open("responses.json", "w") as out:
    json.dump(results, out, indent=2)