import os
from openai import OpenAI

# DEMO: ungoverned / shadow AI proxy using an env key pulled into source paths.
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url="https://api.openai.com/v1")


def relay(prompt: str):
    return client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
    )
