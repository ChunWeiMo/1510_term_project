import json

def savedata(character_dictionary: dict, current_map: dict):
    """
    Save playing data to json file.

    :param character_dictionary: a dictionary of character attributes
    :param current_map: a dictionary
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    :precondition: current_map must have element-coordinate as key-value pair
    :precondition: coordinate must be a tuple of integers
    :postcondition: save character_dictionary to character.json
    :postcondition: save current_map to current_map.json
    :raise TypeError: if current_map is not a dictionary
    """
    if type(current_map) != dict:
        raise TypeError("current_map must be a dictionary")
    with open("./character.json", "w") as file_object:
        json.dump(character_dictionary, file_object)
    converted_map = {str(key): value for key, value in current_map.items()}
    with open("./current_map.json", 'w') as file_object:
        json.dump(converted_map, file_object)
        print(f"Playing data is saved successfully!")
        

def ask_loaddata(character_dictionary: dict, current_map: dict) -> tuple:
    """
    Ask player whether to load playing data or not.

    :param character_dictionary: a dictionary of character attributes
    :param current_map: a dictionary
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    :precondition: current_map must have element-coordinate as key-value pair
    :precondition: coordinate must be a tuple of integers
    :postcondition: input Y to load character_dictionary and current_map playing data
    :return: a tuple
    """
    is_load = input("Unsaved data will be lost.\n Are you sure you want to load savedata? (Y/N)\n")
    if is_load.upper() == "Y":
        character_dictionary, current_map = loaddata()
    return character_dictionary, current_map


def loaddata() -> [tuple, None]:
    """
    Load playing data from json file.

    :postcondition: load character.json and convert to character_dictionary
    :postcondition: load current_map.json and convert to current_map
    :return: a tuple if load playing data successfully
    :return: None if load playing data failed
    """
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
    
