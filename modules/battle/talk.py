"""Talk module
Lvl 1 enemies:
    Slime:
    pixie:
    wolf:
    skeleton:
    ghost:
    golem:

Lvl 2 enemies:
    spider:
    archer:
    spirit:
    succubus:
    maid:
    gargoyle:

"""


from modules.battle import enemy_lines


def talk_to_enemy(character_dictionary, enemy_appeared):
    is_enemy_killed = False
    return is_enemy_killed