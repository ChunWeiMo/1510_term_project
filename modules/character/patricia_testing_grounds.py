# def merchant(character_dictionary):
#     print("\nMerchant: Oh! What are you doing here? You must be a hero!\nCome check out my humble store!")
#     try:
#         response = int(input("What do you want to do?\n"
#                              "[1] Buy\n"
#                              "[2] Battle\n"
#                              "[3] Leave\n"))
#     except ValueError:
#         print("\nPlease enter a number from 1-3.")
#         merchant(character_dictionary)
#     else:
#         if response > 3 or response < 1:
#             print("\nPlease enter a number from 1-3.")
#             merchant(character_dictionary)
#         elif response == 1:
#             buy(character_dictionary)
#         elif response == 2:
#             battle_merchant(character_dictionary)
#         else:
#             leave_merchant()
#
#
# def buy(character_dictionary):
#     print(f"\nMerchant: Welcome!\n"
#           f"You currently have {character_dictionary['Items']['Gold']} gold.")
#     try:
#         buy_response = int(input(f"Merchant: What would you like to buy?\n"
#                                  f"[1] Potion x1 -----10 Gold\n"
#                                  f"[2] Potion x5 -----45 Gold\n"
#                                  f"[3] Potion x10 ----90 Gold\n"
#                                  f"[4] Leave\n"))
#     except ValueError:
#         print("\nPlease enter a number from 1-4.")
#         buy(character_dictionary)
#     else:
#         if buy_response > 4 or buy_response < 1:
#             print("\nPlease enter a number from 1-4.")
#             buy(character_dictionary)
#         elif buy_response == 1:
#             potions = 1
#             check_gold(character_dictionary, potions)
#         elif buy_response == 2:
#             potions = 5
#             check_gold(character_dictionary, potions)
#         elif buy_response == 3:
#             potions = 10
#             check_gold(character_dictionary, potions)
#         else:
#             leave_merchant()
#
#
# def check_gold(character_dictionary, potions):
#     if potions == 1:
#         gold_needed = 10
#     elif potions == 5:
#         gold_needed = 45
#     else:
#         gold_needed = 90
#     if character_dictionary['Items']['Gold'] >= gold_needed:
#         character_dictionary['Items']['Potions'] += potions
#         character_dictionary['Items']['Gold'] -= gold_needed
#         print("\nMerchant: Thank you for your patronage! Come again!")
#     else:
#         print("\nMerchant: You don't have enough gold! Maybe come back later when you have enough.")
#         leave_merchant()
#
#
# def battle_merchant(character_dictionary):
#     print("\nMerchant: What! you're trying to rob me?!\nMerchant: Hmph who do you think I am! "
#           "I stay in the dungeon farming for"
#           "gold day in an day out.\nMerchant: You cannot defeat me!\n")
#     merchant_stats = {"Level": 9999, "HP": 9999, "STR": 50, "DEF": 50, "SPD": 1}
#     turn = "merchant"
#     while merchant_stats["HP"] > 0 and character_dictionary["Character_status"]["HP"] > 0:
#         if turn == "character":
#             if character_dictionary["Character_status"]["STR"] - merchant_stats["DEF"] <= 0:
#                 damage = 1
#             else:
#                 damage = character_dictionary["Character_status"]["STR"] - merchant_stats["DEF"]
#             merchant_stats["HP"] -= damage
#             print(f"You deal {damage} damage to Merchant!\n"
#                   f"Merchant has {merchant_stats['HP']} HP left.")
#             turn = "merchant"
#         else:
#             if merchant_stats["STR"] - character_dictionary["Character_status"]["DEF"] <= 0:
#                 damage = 1
#             else:
#                 damage = merchant_stats["STR"] - character_dictionary["Character_status"]["DEF"]
#             character_dictionary["Character_status"]["HP"] -= damage
#             if character_dictionary['Character_status']['HP'] > 0:
#                 print(f"Merchant dealt {damage} damage to you!\n"
#                       f"You have {character_dictionary['Character_status']['HP']} HP left.")
#             else:
#                 print(f"Merchant dealt {damage} damage to you!\n"
#                       f"You now have 0 HP left.")
#             turn = "character"
#     if character_dictionary["Character_status"]["HP"] == 0:
#         return
#
#
# def leave_merchant():
#     print("\nMerchant: Thanks for stopping by!")


def main():
    character_dictionary = {"Character_status": {"Level": 1, "HP": 50, "STR": 1,
                                                 "DEF": 1, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3},
                            "X-coordinate": 0,
                            "Y-coordinate": 0,
                            "EXP": 0,
                            "Items": {"Gold": 0, "Potions": 0},
                            "Equipment": 0
                            }
    merchant(character_dictionary)
    print(character_dictionary)


if __name__ == "__main__":
    main()
