import json


def savedata(character_dictionary, current_map):
    with open("./savedata/character.json","w") as file_object:
        json.dump(character_dictionary, file_object)
        converted_map = {str(key): value for key, value in current_map.items()}
    with open("./savedata/current_map.json", 'w') as file_object:
        json.dump(converted_map, file_object)
        print(f"Playing data is saved successfully!")
        

def loaddata(character_1, current_map):
    is_load = input(("Unsaved data will be lost.\n Are you sure you want to load savedata? (Y/N)"))
    if is_load.upper() == "Y":
        print("Loading savedata...\n")
        try:
            with open("./savedata/character.json") as file_object:
                character_dictionary = json.load(file_object)
            with open("./savedata/current_map.json") as file_object:
                converted_map = json.load(file_object)
        except FileNotFoundError:
            print("savedata does not exist")
        else:
            current_map = dict()
            for key in converted_map:
                current_map[tuple((int(key[1]), int(key[-2])))] = converted_map[key]
            return character_dictionary, current_map
    else:
        return character_1, current_map
