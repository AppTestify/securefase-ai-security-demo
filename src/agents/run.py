import os
import subprocess
from openai import OpenAI

client = OpenAI()


def solve(task):
    # DEMO: model output is executed as code / shell.
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": task}],
    )
    code = response.choices[0].message.content
    exec(code)
    subprocess.run(code, shell=True)
    os.system(code)
