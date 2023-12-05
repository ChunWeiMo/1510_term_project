import json


def savedata(character_dictionary, current_map):
    with open("./character.json","w") as file_object:
        json.dump(character_dictionary, file_object)
        converted_map = {str(key): value for key, value in current_map.items()}
    with open("./current_map.json", 'w') as file_object:
        json.dump(converted_map, file_object)
        print(f"Playing data is saved successfully!")
        

def ask_loaddata(character_dictionary, current_map):
    is_load = input(("Unsaved data will be lost.\n Are you sure you want to load savedata? (Y/N)\n"))
    if is_load.upper() == "Y":
        character_dictionary, current_map = loaddata()
    return character_dictionary, current_map
    
def loaddata():
    print("Loading savedata...\n")
    try:
        with open("./character.json") as file_object:
            character_dictionary = json.load(file_object)
        with open("./current_map.json") as file_object:
            converted_map = json.load(file_object)
    except FileNotFoundError:
        print("savedata does not exist")
        return
    else:
        current_map = dict()
        for key in converted_map:
            current_map[tuple((int(key[1]), int(key[-2])))] = converted_map[key]
        return character_dictionary, current_map
    
