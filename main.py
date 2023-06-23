import os
import datetime

from api_handler import OpenAiApiHandler
from result_processor import ResultProcessor
from chat_manager import ChatManager



OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

context = "Imagine you are software engineer \n"
context += "working in order to create test automation framework to test UI of a mobile app \n"

prompt = "Imagine you are software engineer \n"
prompt += "working in order to create test automation framework to test UI of a mobile app \n"
prompt += "Use java as a test automation language \n"
prompt += "1 Define framework layers \n"
prompt += "2 Define framework components and choose most advanced example for each component (but use Junit 5 as a runner) \n"
prompt += "3 Describe reasonable framework structure (how it should look in terms of files and folders) and picture it in ascii way\n"
prompt += "4 Create pom.xml \n"
prompt += "5 Write all classes (Java files), you stipulated on a 3rd step using chosen on 4th step dependencies and simple test for mobile app\n"

if __name__ == "__main__":
    chat_manager = ChatManager()
    chat_manager.add_system_message(context)
    chat_manager.add_user_message(prompt)

    handler = OpenAiApiHandler(OPENAI_API_KEY)
    response = handler.generate_chat_response(chat_manager.get_messages())
    processed_response = ResultProcessor.process_response(response)

    print(prompt)
    print('---------------------------------------------------------------------------------------------------------')
    print(processed_response)

    current_datetime = datetime.datetime.now()
    filename = current_datetime.strftime("%Y-%m-%d_%H-%M-%S.txt")

    file = open(filename, 'w')
    file.write(context)
    file.write(prompt)
    file.write('---------------------------------------------------------------------------------------------------------')
    file.write(processed_response)
    file.close()
