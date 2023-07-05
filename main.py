import os
import datetime

from api_handler import OpenAiApiHandler
from result_processor import ResultProcessor
from chat_manager import ChatManager



OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

request_id = 1

with open(f'request/context{request_id}.txt', 'r') as file:
    context = file.read()

with open(f'request/prompt{request_id}.txt', 'r') as file:
    prompt = file.read()

with open(f'request/payload{request_id}.txt', 'r') as file:
    payload = file.read()


if __name__ == "__main__":
    chat_manager = ChatManager()
    chat_manager.add_system_message(context)
    chat_manager.add_user_message(prompt)
    chat_manager.add_user_message(payload)

    handler = OpenAiApiHandler(OPENAI_API_KEY)
    response = handler.generate_chat_response(chat_manager.get_messages())
    processed_response = ResultProcessor.process_response(response)

    print(context)
    print(prompt)
    print(payload)
    print('---------------------------------------------------------------------------------------------------------\n')
    print(processed_response)

    current_datetime = datetime.datetime.now()
    filename = current_datetime.strftime("output/%Y-%m-%d_%H-%M-%S.txt")

    file = open(filename, 'w')
    file.write("context " + context)
    file.write("prompt " + prompt)
    file.write("payload " + payload)
    file.write('---------------------------------------------------------------------------------------------------------\n')
    file.write(processed_response)
    file.close()
