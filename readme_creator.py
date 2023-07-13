import os
import json
from request_maker import get_file_description

PROMPT_FILE_DESCR = """
You will receive a file's content as a text.
Generate a description of file: straight - what code in this file is doing in 3 sentences. 
"""

PROMPT_PROJECT_DESCR = """
You will receive a file's content as a text - it is a repository of some kind of service related to chess data processing.
Information presented in the json following form:

    "analysis": {
        "analyzer.js": {
            "content": "const analysisQueue = require('./analysis-queue');\nconst converter = require('../converter');\nconst depthSelector = require('./depth-selector');\nconst pgnAnalyzer = require('./pgn-analyzer');\n\nlet ricpaClient;\nlet pingUrl;\n\nfunction analyze(item) {\n  if(ricpaClient) {\n    if(pgnAnalyzer.areMovesWithinLimit(item.moves)) {\n      item.pingUrl = pingUrl;\n      console.log(`POST '${item.fen}' w/ depth ${item.depth} to ${ricpaClient.config.fullpath}`);\n      ricpaClient.postFen(item);\n    } else {\n      console.log(`too long pgn for opening for analysis: ${item.moves.join(',')}`);\n      analysisQueue.delete(item.fen);\n    }\n  } else {\n    console.error('set ricpaClient settings in app.config.json to analyze positions');\n  }\n}\n\nconst analyzeLater = function(moves, base, priority) {\n  return new Promise((resolve, reject) => {\n    if (moves) {\n      if (!base) reject('analyzeLater is called with moves without base');\n      try {\n        let movesList = pgnAnalyzer.splitSequentially(base, moves);\n        movesList = movesList.filter(pgnAnalyzer.areMovesWithinLimit);\n        movesList.forEach(function(moves) {\n          const queueItem = {\n            fen: converter.moves2fen(moves),\n            moves,\n            depth: depthSelector.getMinDepthRequired()\n          };\n          analysisQueue.add(queueItem, priority);\n        });\n      }\n      catch (err) {\n        reject(err);\n      }\n      resolve();\n    } else {\n      reject();\n    }\n  });\n};\n\nfunction setSettings(settings) {\n  ricpaClient = settings.ricpaClient;\n  pingUrl = settings.pingUrl;\n}\n\nmodule.exports = { analyze, analyzeLater, setSettings};\n\n"
        },
        "queue-serializer.js": {
            "content": "const smartStringifier = require('smart-stringifier');\n\nmodule.exports.stringify = function(queue) {\n  return smartStringifier.stringify({q: queue});\n};\n\nmodule.exports.parse = function(str) {\n  const parsed = JSON.parse(str).q;\n  parsed[2]=[];\n  parsed[3]=[];\n  return parsed;\n};\n"
        },

where "analysis" - folder name

and

        "analyzer.js": {
            "content": "const analysisQueue = require('./analysis-queue');\nconst converter = require('../converter');\nconst depthSelector = require('./depth-selector');\nconst pgnAnalyzer = require('./pgn-analyzer');\n\nlet ricpaClient;\nlet pingUrl;\n\nfunction analyze(item) {\n  if(ricpaClient) {\n    if(pgnAnalyzer.areMovesWithinLimit(item.moves)) {\n      item.pingUrl = pingUrl;\n      console.log(`POST '${item.fen}' w/ depth ${item.depth} to ${ricpaClient.config.fullpath}`);\n      ricpaClient.postFen(item);\n    } else {\n      console.log(`too long pgn for opening for analysis: ${item.moves.join(',')}`);\n      analysisQueue.delete(item.fen);\n    }\n  } else {\n    console.error('set ricpaClient settings in app.config.json to analyze positions');\n  }\n}\n\nconst analyzeLater = function(moves, base, priority) {\n  return new Promise((resolve, reject) => {\n    if (moves) {\n      if (!base) reject('analyzeLater is called with moves without base');\n      try {\n        let movesList = pgnAnalyzer.splitSequentially(base, moves);\n        movesList = movesList.filter(pgnAnalyzer.areMovesWithinLimit);\n        movesList.forEach(function(moves) {\n          const queueItem = {\n            fen: converter.moves2fen(moves),\n            moves,\n            depth: depthSelector.getMinDepthRequired()\n          };\n          analysisQueue.add(queueItem, priority);\n        });\n      }\n      catch (err) {\n        reject(err);\n      }\n      resolve();\n    } else {\n      reject();\n    }\n  });\n};\n\nfunction setSettings(settings) {\n  ricpaClient = settings.ricpaClient;\n  pingUrl = settings.pingUrl;\n}\n\nmodule.exports = { analyze, analyzeLater, setSettings};\n\n"
        },
            
is a file in a folder with is content

folders may contain another folders with files. 
generate a README.MD file:
- explain what service is for (based on a content of files), for each files make 2 or 3 sentences 
- write how to start it

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


folder = ""
path = f'/Users/vladimirklonin/IdeaProjects/main/chegura/app/{folder}'
output_file = f'folder_structure_{folder}.json'
create_json_file(path, output_file)
process_json_file(output_file, folder)
