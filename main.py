import os

import requests

# OpenAI API endpoint and authentication key
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


def send_openai_request(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    data = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 3000,
        "temperature": 1,
    }

    response = requests.post(OPENAI_API_URL, headers=headers, json=data)
    return response.json()


def send_openai_get_request(openai_url):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    response = requests.get(openai_url, headers=headers)
    return response.json()


def print_openai_response(response):
    if 'choices' in response:
        for choice in response['choices']:
            completion = choice['text'].strip()
            print(completion)
    else:
        print(response)  # Handle error responses


def main():
    prompt = "Imagine you are software engineer \n"
    prompt += "working in order to create test automation framework to test UI of a mobile app \n"
    prompt += "Use java as a test automation language \n"
    prompt += "1 Define framework layers \n"
    prompt += "2 Define framework components and choose most advanced example for each component (but use Junit as a runner) \n"
    prompt += "3 Describe reasonable framework structure (how it should look in terms of files and folders) and picture it in ascii way\n"
    prompt += "4 Create pom.xml \n"
    prompt += "5 Write all necessary classes shown on a 3rd step using chosen on 4th step dependencies and simple test for mobile app\n"

    response = send_openai_request(prompt)

    print(prompt)
    print('---------------------------------------------------------------------------------------------------------')

    print_openai_response(response)


if __name__ == "__main__":
    main()
