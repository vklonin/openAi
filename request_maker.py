import os

import openai

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


def get_file_description(prompt, content) -> str:
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": content}
    ]

    openai.api_key = OPENAI_API_KEY
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages
    )

    return res["choices"][0]["message"]["content"]
