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


def enemy_dialogue():
    # Lvl 1 enemies
    slime_chat = {
        "Question": "Plip plop plip plop~~",
        "Answer 1": "*Pat it*",
        "Answer 2": "*Squeeze it*",
        "Answer 3": "*kick it*",
        "Reply 1": "Pliippp! (it looks happy)",
        "Reply 2": "PLIPP! (battle)",
        "Reply 2.1": "Pliiiipppp~ (it looks content)",
        "Reply 3": "GRRrr (battle)",
        "Reply 3.1": "plip..(it looks sad and scared)"}
    pixie_chat = {
        "Question": "",
        "Answer 1": "",
        "Answer 2": "",
        "Answer 3": "",
        "Reply 1": "",
        "Reply 2": "",
        "Reply 2.1": "",
        "Reply 3": "",
        "Reply 3.1": ""}
    wolf_chat = {
        "Question": "",
        "Answer 1": "",
        "Answer 2": "",
        "Answer 3": "",
        "Reply 1": "",
        "Reply 2": "",
        "Reply 2.1": "",
        "Reply 3": "",
        "Reply 3.1": ""}
    skeleton_chat = {
        "Question": "",
        "Answer 1": "",
        "Answer 2": "",
        "Answer 3": "",
        "Reply 1": "",
        "Reply 2": "",
        "Reply 2.1": "",
        "Reply 3": "",
        "Reply 3.1": ""}
    ghost_chat = {
        "Question": "",
        "Answer 1": "",
        "Answer 2": "",
        "Answer 3": "",
        "Reply 1": "",
        "Reply 2": "",
        "Reply 2.1": "",
        "Reply 3": "",
        "Reply 3.1": ""}
    golem_chat = {
        "Question": "",
        "Answer 1": "",
        "Answer 2": "",
        "Answer 3": "",
        "Reply 1": "",
        "Reply 2": "",
        "Reply 2.1": "",
        "Reply 3": "",
        "Reply 3.1": ""}

    # Lvl 2 enemies
    spider_chat = {
        "Question": "",
        "Answer 1": "",
        "Answer 2": "",
        "Answer 3": "",
        "Reply 1": "",
        "Reply 2": "",
        "Reply 2.1": "",
        "Reply 3": "",
        "Reply 3.1": ""}
    archer_chat = {
        "Question": "",
        "Answer 1": "",
        "Answer 2": "",
        "Answer 3": "",
        "Reply 1": "",
        "Reply 2": "",
        "Reply 2.1": "",
        "Reply 3": "",
        "Reply 3.1": ""}
    spirit_chat = {
        "Question": "",
        "Answer 1": "",
        "Answer 2": "",
        "Answer 3": "",
        "Reply 1": "",
        "Reply 2": "",
        "Reply 2.1": "",
        "Reply 3": "",
        "Reply 3.1": ""}
    succubus_chat = {
        "Question": "",
        "Answer 1": "",
        "Answer 2": "",
        "Answer 3": "",
        "Reply 1": "",
        "Reply 2": "",
        "Reply 2.1": "",
        "Reply 3": "",
        "Reply 3.1": ""}
    maid_chat = {
        "Question": "",
        "Answer 1": "",
        "Answer 2": "",
        "Answer 3": "",
        "Reply 1": "",
        "Reply 2": "",
        "Reply 2.1": "",
        "Reply 3": "",
        "Reply 3.1": ""}
    gargoyle_chat = {
        "Question": "",
        "Answer 1": "",
        "Answer 2": "",
        "Answer 3": "",
        "Reply 1": "",
        "Reply 2": "",
        "Reply 2.1": "",
        "Reply 3": "",
        "Reply 3.1": ""}

    # Miniboss
    cerberus_chat = {
        "Question 1":
            {"Question": "",
            "Answer 1": "",
            "Answer 2": "",
            "Answer 3": "",
            "Reply 1": "",
            "Reply 2": "",
            "Reply 2.1": "",
            "Reply 3": "",
            "Reply 3.1": ""},
        "Questions 2":
            {"Question": "",
            "Answer 1": "",
            "Answer 2": "",
            "Answer 3": "",
            "Reply 1": "",
            "Reply 2": "",
            "Reply 2.1": "",
            "Reply 3": "",
            "Reply 3.1": ""},
        "Question 3":
            {"Question": "",
            "Answer 1": "",
            "Answer 2": "",
            "Answer 3": "",
            "Reply 1": "",
            "Reply 2": "",
            "Reply 2.1": "",
            "Reply 3": "",
            "Reply 3.1": ""}}
    oberon_chat = {
        "Question 1":
            {"Question": "",
            "Answer 1": "",
            "Answer 2": "",
            "Answer 3": "",
            "Reply 1": "",
            "Reply 2": "",
            "Reply 2.1": "",
            "Reply 3": "",
            "Reply 3.1": ""},
        "Questions 2":
            {"Question": "",
            "Answer 1": "",
            "Answer 2": "",
            "Answer 3": "",
            "Reply 1": "",
            "Reply 2": "",
            "Reply 2.1": "",
            "Reply 3": "",
            "Reply 3.1": ""},
        "Question 3":
            {"Question": "",
            "Answer 1": "",
            "Answer 2": "",
            "Answer 3": "",
            "Reply 1": "",
            "Reply 2": "",
            "Reply 2.1": "",
            "Reply 3": "",
            "Reply 3.1": ""}}
    dracula_chat = {
        "Question 1":
            {"Question": "",
            "Answer 1": "",
            "Answer 2": "",
            "Answer 3": "",
            "Reply 1": "",
            "Reply 2": "",
            "Reply 2.1": "",
            "Reply 3": "",
            "Reply 3.1": ""},
        "Questions 2":
            {"Question": "",
            "Answer 1": "",
            "Answer 2": "",
            "Answer 3": "",
            "Reply 1": "",
            "Reply 2": "",
            "Reply 2.1": "",
            "Reply 3": "",
            "Reply 3.1": ""},
        "Question 3":
            {"Question": "",
            "Answer 1": "",
            "Answer 2": "",
            "Answer 3": "",
            "Reply 1": "",
            "Reply 2": "",
            "Reply 2.1": "",
            "Reply 3": "",
            "Reply 3.1": ""}}

    # Final Boss
    dragon_chat = {
        "Question 1":
            {"Question": "",
            "Answer 1": "",
            "Answer 2": "",
            "Answer 3": "",
            "Reply 1": "",
            "Reply 2": "",
            "Reply 2.1": "",
            "Reply 3": "",
            "Reply 3.1": ""},
        "Questions 2":
            {"Question": "",
            "Answer 1": "",
            "Answer 2": "",
            "Answer 3": "",
            "Reply 1": "",
            "Reply 2": "",
            "Reply 2.1": "",
            "Reply 3": "",
            "Reply 3.1": ""},
        "Question 3":
            {"Question": "",
            "Answer 1": "",
            "Answer 2": "",
            "Answer 3": "",
            "Reply 1": "",
            "Reply 2": "",
            "Reply 2.1": "",
            "Reply 3": "",
            "Reply 3.1": ""},
        "Questions 4":
            {"Question": "",
             "Answer 1": "",
             "Answer 2": "",
             "Answer 3": "",
             "Reply 1": "",
             "Reply 2": "",
             "Reply 2.1": "",
             "Reply 3": "",
             "Reply 3.1": ""},
        "Question 5":
            {"Question": "",
             "Answer 1": "",
             "Answer 2": "",
             "Answer 3": "",
             "Reply 1": "",
             "Reply 2": "",
             "Reply 2.1": "",
             "Reply 3": "",
             "Reply 3.1": ""}}


def talk_to_enemy(character_dictionary, enemy_appeared):
    pass
