import json

def loadScript(script_name : str):
  with open("../data/scripts.json") as script_file:
    script = json.load(script_file)
    return script[script_name]