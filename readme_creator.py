import os
import json


def create_folder_structure(path, folder_structure):
    for item in os.scandir(path):
        if item.is_file():
            folder_structure.append(item.name)
        elif item.is_dir():
            sub_folder_structure = []
            folder_structure.append({
                item.name: create_folder_structure(item.path, sub_folder_structure)
            })
    return folder_structure


def create_json_file(path_to, output_file_out):
    folder_structure = create_folder_structure(path_to, [])
    with open(output_file_out, 'w') as file:
        json.dump(folder_structure, file, indent=4)


# Usage example:
path = '/Users/vladimirklonin/IdeaProjects/SPARK/test-commons'
output_file = 'folder_structure.json'
create_json_file(path, output_file)
