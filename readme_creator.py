import os
import json
from request_maker import get_file_description

PROMPT_FILE_DESCR = """
You will receive a file's content as a text. This is a one file from a repository, containing a code on some programming language.
Generate a description of file - what this code is doing and what it for: short and straight explanation without comments, no more than 5 sentences. Keep in mind that this description will be used to do a summary
"""

PROMPT_PROJECT_DESCR = """
You will receive a file's content as a text - it is a repository of some kind of service related to chess data processing.
Information presented in the json following form:

{
    "analysis": {
        "analyzer.js": {
            "description": "This code defines several functions and exports them as module exports. The `analyze` function takes an item as an argument and checks if `ricpaClient` is set. If it is, the function checks if the moves in the item are within a limit and, if so, sets the `pingUrl` property of the item and posts it to the `ricpaClient`. If the moves are too long, the item is deleted from the analysis queue. If `ricpaClient` is not set, an error is logged. The `analyzeLater` function takes moves, a base, and a priority as arguments and returns a promise. It splits the moves sequentially, filters them based on a limit, and adds them to the analysis queue. The `setSettings` function takes a settings object and sets the `ricpaClient` and `pingUrl` variables."
        },
        "queue-serializer.js": {
            "description": "This code is a module that provides two functions for stringifying and parsing queue data. The `stringify` function takes a queue object as input and uses a smart stringifier library to convert it into a string. The `parse` function takes a string as input, parses it into a JSON object, and extracts the `q` property. It then modifies the extracted queue by setting the elements at index 2 and 3 to empty arrays, and returns the modified queue."
        },
        "endgame-analyzer.js": {
            "description": "This code is a module that analyzes whether a given chess position is in the endgame phase. It uses the package `fen-analyzer` to get the count of pieces on the board. If the count is less than or equal to 7, it determines that the position is in the endgame."
        }, ...
        
where "analysis" - folder name

and
        "analyzer.js": {
            "description": "This code defines several functions and exports them as module exports. The `analyze` function takes an item as an argument and checks if `ricpaClient` is set. If it is, the function checks if the moves in the item are within a limit and, if so, sets the `pingUrl` property of the item and posts it to the `ricpaClient`. If the moves are too long, the item is deleted from the analysis queue. If `ricpaClient` is not set, an error is logged. The `analyzeLater` function takes moves, a base, and a priority as arguments and returns a promise. It splits the moves sequentially, filters them based on a limit, and adds them to the analysis queue. The `setSettings` function takes a settings object and sets the `ricpaClient` and `pingUrl` variables."
        },
            
is a file in a folder with a description of file made as a short summary

folders may contain another folders with files. 
generate a README.MD file as following:
- Use following template for README.MD and based on an information provided in a json - fill it.
- use section description to generate data:
Section and section description example : ## Running the tests
Explain how to run the automated tests for this system.


If you do not find in json anything related to a section mentioned in a template.MD - omit this section in a resulting README.MD file, but keep Versioning, Authors, License and Acknowledgments
change table of content accordingly

<start of template.MD>
"""


def create_folder_structure(path, folder_structure):
    for item in os.scandir(path):
        if item.name.startswith('.'):
            continue
        if item.is_file():
            file_extension = os.path.splitext(item.name)[1]
            if file_extension.lower() in ('.java', '.groovy', '.js'):
                with open(item.path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                    file_description = get_file_description(PROMPT_FILE_DESCR, file_content)

                folder_structure[item.name] = {
                    # "content": file_content,
                    "description": file_description
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
    with open(output_file_in, 'r', encoding='utf-8') as file, open('template.MD', 'r', encoding='utf-8') as template:
        res = get_file_description(PROMPT_PROJECT_DESCR + template.read(), file.read())
    with open(f'README_{folder}.MD', 'w') as file:
        file.write(res)


folder = ""
path = f'/Users/vladimirklonin/IdeaProjects/main/chegura/app/{folder}'
output_file = f'folder_structure_{folder}.json'
create_json_file(path, output_file)
process_json_file(output_file, folder)
