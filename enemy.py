"""
Enemy module.
"""


def enemy():
    slime = {"HP": 10, "STR": 6, "DEF": 1, "SPD": 2}
    pixie = {"HP": 6, "STR": 2, "DEF": 1, "SPD": 3}
    wolf = {"HP": 15, "STR": 3, "DEF": 1, "SPD": 2}
    skeleton = {"HP": 15, "STR": 2, "DEF": 2, "SPD": 2}
    ghost = {"HP": 10, "STR": 2, "DEF": 0, "SPD": 4}
    golem = {"HP": 20, "STR": 1, "DEF": 5, "SPD": 0}

    cave_spider = {"HP": 25, "STR": 1, "DEF": 2, "SPD": 5}
    skeleton_archer = {"HP": 20, "STR": 4, "DEF": 0, "SPD": 4}
    restless_spirit = {"HP": 30, "STR": 4, "DEF": 1, "SPD": 3}
    succubus = {"HP": 20, "STR": 3, "DEF": 1, "SPD": 4}
    dungeon_maid = {"HP": 25, "STR": 3, "DEF": 3, "SPD": 2}
    gargoyle = {"HP": 40, "STR": 2, "DEF": 6, "SPD": 0}

    cerberus = {"HP": 50, "STR": 5, "DEF": 5, "SPD": 0}  # special: attack will cause burn for extra 1 dmg
    oberon = {"HP": 40, "STR": 4, "DEF": 0, "SPD": 6}  # special: summons 2 pixies every 3 turns
    dracula = {"HP": 40, "STR": 5, "DEF": 1, "SPD": 4}  # special: gains 1 HP after attack

    dragon = {"HP": 100, "STR": 7, "DEF": 4, "SPD": 3}  # 3 special moves

    enemy_dictionary = {
        "Level 1": {1: slime, 2: pixie, 3: wolf, 4: skeleton, 5: ghost, 6: golem},
        "Level 2": {1: cave_spider, 2: skeleton_archer, 3: restless_spirit, 4: succubus, 5: dungeon_maid, 6: gargoyle},
        "Miniboss": {1: cerberus, 2: oberon, 3: dracula},
        "Final Boss": dragon
    }
    return enemy_dictionary
