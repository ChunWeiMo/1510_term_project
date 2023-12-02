# def use_potion(character_dictionary):
#     if character_dictionary["Character_status"]["Level"] == 1:
#         max_hp = 100
#     elif character_dictionary["Character_status"]["Level"] == 2:
#         max_hp = 120
#     else:
#         max_hp = 150
#
#     if character_dictionary["Items"]["Potions"] > 0:
#         response = None
#         while response is None:
#             response = ask_player_potions(character_dictionary)
#         heal_character(character_dictionary, response, max_hp)
#     else:
#         print("\nYou have 0 potions to use.")
#     return
#
#
# def ask_player_potions(character_dictionary):
#     try:
#         response = int(input(f"\nYou have {character_dictionary['Items']['Potions']} potions and "
#                              f"{character_dictionary['Character_status']['HP']} HP.\n"
#                              f"Enter how many potions you would like to use:\n"))
#     except ValueError:
#         print("\nPlease enter the amount of potions as a number.")
#     else:
#         while response <= 0 or response > character_dictionary['Items']['Potions']:
#             print(f"\nYou must enter a number between 1 and {character_dictionary['Items']['Potions']}.")
#             response = int(input(f"\nEnter how many potions you would like to use:\n"))
#         return response
#
#
# def heal_character(character_dictionary, response, max_hp):
#     if character_dictionary["Character_status"]["HP"] <= max_hp - response * 20:
#         character_dictionary["Character_status"]["HP"] += response * 20
#     else:
#         character_dictionary["Character_status"]["HP"] = max_hp
#     character_dictionary['Items']['Potions'] -= response
#     print(f"\nYour HP is now {character_dictionary['Character_status']['HP']} and you have "
#           f"{character_dictionary['Items']['Potions']} potions left.")


# def main():
#     character_dictionary = {"Character_status": {"Level": 3, "HP": 50, "STR": 1,
#                                                  "DEF": 1, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3},
#                             "X-coordinate": 0,
#                             "Y-coordinate": 0,
#                             "EXP": 0,
#                             "Items": {"Gold": 0, "Potions": 10},
#                             "Equipment": 0
#                             }
#     use_potion(character_dictionary)
#     print(character_dictionary)
#
#
# if __name__ == "__main__":
#     main()
