# starting file

import json_reader

link = str(input('put the path here - '))
obj_json = json_reader.Json(link)
obj_json.read()

