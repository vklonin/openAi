import openai

class OpenAiApiHandler:

    def __init__(self, api_key, model="gpt-3.5-turbo-16k", temperature=0, max_tokens=5000):
        openai.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate_chat_response(self, messages):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )

        return response['choices'][0]['message']['content']