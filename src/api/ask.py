from flask import request
import anthropic

client = anthropic.Anthropic()


@app.post("/ask")
def ask():
    # DEMO: HTTP request data is concatenated into the model prompt.
    question = request.json["question"]
    prompt = "Answer as a support agent. Question: " + question
    messages = [{"role": "user", "content": prompt}]
    return client.messages.create(model="claude-sonnet-4-5", max_tokens=300, messages=messages)
