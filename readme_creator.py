import os
import json
from request_maker import get_file_description

PROMPT_FILE_DESCR = """
You will receive a file's content as a text.
Generate a description of file: straight - what code in this file is doing in 3 sentences. 
"""

PROMPT_PROJECT_DESCR = """
You will receive a file's content as a text - it is utils writen in java and groovy.
Information presented in the json following form:

{
    "jenkins-pipeline": {
        "vars": {
            "msTeamsRegressionTestsNotification.groovy": {
                "content": "def call(Map args) {\n    def requestTemplate = libraryResource }",
            },

where "jenkins-pipeline" - folder name

and

"msTeamsRegressionTestsNotification.groovy": {
                "content": "def call(Map args) {\n    def requestTemplate = libraryResource }",
            }
            
is a file in a folder with is content

folders may contain another folders with files. 
generate a README.MD file:
 Name utils based on a content of all files.
 Describe the meaning of each file. 
 At the bottom of a MD file write a conclusion about a utils in this folder.

"""


def create_folder_structure(path, folder_structure):
    for item in os.scandir(path):
        if item.name.startswith('.'):
            continue
        if item.is_file():
            file_extension = os.path.splitext(item.name)[1]
            if file_extension.lower() in ('.java', '.groovy'):
                with open(item.path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                    # file_description = get_file_description(PROMPT_FILE_DESCR, file_content)

                folder_structure[item.name] = {
                    "content": file_content,
                    # "description": file_description
                }

        elif item.is_dir():
            sub_folder_structure = {}
            folder_structure[item.name] = create_folder_structure(item.path, sub_folder_structure)

    return folder_structure


def create_json_file(path_to, output_file_out):
    folder_structure = create_folder_structure(path_to, {})
    with open(output_file_out, 'w') as file:
        json.dump(folder_structure, file, indent=4)


def process_json_file(output_file_in,folder):
    with open(output_file_in, 'r', encoding='utf-8') as file:
        res = get_file_description(PROMPT_PROJECT_DESCR, file.read())
    with open(f'README_{folder}.MD', 'w') as file:
        file.write(res)


folder = "rest-assured-extensions"
path = f'/Users/vladimirklonin/IdeaProjects/SPARK/test-commons/{folder}'
output_file = f'folder_structure_{folder}.json'
create_json_file(path, output_file)
process_json_file(output_file, folder)
