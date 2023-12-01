"""For enemy talk"""


def enemy_lines():
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
        "Question": "What do you think of fairies?",
        "Answer 1": "They're really cute!",
        "Answer 2": "They like to steal teeth?",
        "Answer 3": "I wanna pluck out their wings...",
        "Reply 1": "Aww thanks!",
        "Reply 2": "Eww that's just a myth!",
        "Reply 2.1": "Hmph how could you say that, I'm leaving.",
        "Reply 3": "What! No! I'm gonna pluck out your arms!",
        "Reply 3.1": "Noo! Leave me alone please..."}
    wolf_chat = {
        "Question": "Can I take a bite out of you?",
        "Answer 1": "Sure...(-1HP)",
        "Answer 2": "No way!!!",
        "Answer 3": "Are you serious...what an idiot!",
        "Reply 1": "Thanks, I was soo hungry!",
        "Reply 2": "Then I'll have to take it by force!",
        "Reply 2.1": "Ok...guess I'll just starve.",
        "Reply 3": "Looks like you need a lesson in manners!",
        "Reply 3.1": "Yes, that's me...I am an idiot sandwich."}
    skeleton_chat = {
        "Question": "Why do skeletons go together to church to make music?",
        "Answer 1": "They don't have any organs.",
        "Answer 2": "They have no body else to go with!",
        "Answer 3": "They are bone deaf.",
        "Reply 1": "Heehee.",
        "Reply 2": "Are you saying I have no friends!?",
        "Reply 2.1": "Why don't you be my friend then...",
        "Reply 3": "That's not even funny!",
        "Reply 3.1": "Good try I guess..."}
    ghost_chat = {
        "Question": "Have you seen my child?",
        "Answer 1": "No, I'll help you search!",
        "Answer 2": "No idea.",
        "Answer 3": "You're dead already.",
        "Reply 1": "Thank you...",
        "Reply 2": "So heartless!!!",
        "Reply 2.1": "Where is my child...",
        "Reply 3": "YOU LIARRR-!",
        "Reply 3.1": "What...are you serious..."}
    golem_chat = {
        "Question": "You shall not pass. Without the password. The most perfect number.",
        "Answer 1": "1.61803",
        "Answer 2": "3.14159",
        "Answer 3": "6.67430",
        "Reply 1": "Yes. A most perfect shape.",
        "Reply 2": "IncORRect.",
        "Reply 2.1": "NOT PeRFECT. Humans sure do love pies.",
        "Reply 3": "InCORRecT",
        "Reply 3.1": "INCorreCt. Important but not beautiful."}

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
        "Question": "Can I have some gold?",
        "Answer 1": "Ok, if you leave me alone (-10 G)",
        "Answer 2": "No way, bony.",
        "Answer 3": "You should be giving ME gold!",
        "Reply 1": "Hehe, thanks~",
        "Reply 1.1": "You don't have any don't lie to me!!!",
        "Reply 2": "I'll turn you into bones too!!",
        "Reply 2.1": "Uhh, ok then.",
        "Reply 3": "I don't have any! Why do you think I'm asking you??",
        "Reply 3.1": "EEEK! Yessir! (+5 G)"}
    spirit_chat = {
        "Question": "AHHHHHHHHHHHHHHHH!! WHERE IS HE!!",
        "Answer 1": "He is waiting for you behind the door.",
        "Answer 2": "Who?",
        "Answer 3": "He's gone now.",
        "Reply 1": "AHHHHHHHH!!! I'M GOING TO KILL HIM!!!!!",
        "Reply 2": "DON'T LIE!! IHATEHIMHATEHATEHATEHATEKILL!!",
        "Reply 2.1": "I WILL NEVER STOP LOOKING FOR HIM!!!",
        "Reply 3": "NOOOO I WANTED TO KILL HIM MYSELF!!!! WHYYYY!!!",
        "Reply 3.1": "I CAN'T STAND IT!!! I MUST MOVE ON TO KILL HIM IN THE NEXT LIFE!!!!"}
    succubus_chat = {
        "Question": "Why not come to my place and relax for a while? Sweet adventurer~♥",
        "Answer 1": "Sure ♥(-2HP)",
        "Answer 2": "",
        "Answer 3": "",
        "Reply 1": "Such a lovely and tasty adventurer~♥",
        "Reply 2": "",
        "Reply 2.1": "",
        "Reply 3": "",
        "Reply 3.1": ""}
    maid_chat = {
        "Question": "Good afternoon adventurer! What brings you here?",
        "Answer 1": "",
        "Answer 2": "",
        "Answer 3": "",
        "Reply 1": "",
        "Reply 2": "",
        "Reply 2.1": "",
        "Reply 3": "",
        "Reply 3.1": ""}
    gargoyle_chat = {
        "Question": "...",
        "Answer 1": "What a beautiful statue!",
        "Answer 2": "What a hideous statue!",
        "Answer 3": "...",
        "Reply 1": "...",
        "Reply 2": "How dare you!!!!",
        "Reply 2.1": "...",
        "Reply 3": "Don't ignore me!",
        "Reply 3.1": "..."}

    # Miniboss
    cerberus_chat = {
        "Question 1":
            {"Question": "",
             "Answer 1": "",
             "Answer 2": "",
             "Answer 3": "",
             "Reply 1": "",
             "Reply 1.1": "",
             "Reply 2": "",
             "Reply 2.1": "",
             "Reply 3": "",
             "Reply 3.1": ""},
        "Question 2":
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
             "Reply 1.1": "",
             "Reply 2": "",
             "Reply 2.1": "",
             "Reply 3": "",
             "Reply 3.1": ""},
        "Question 2":
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
             "Reply 1.1": "",
             "Reply 2": "",
             "Reply 2.1": "",
             "Reply 3": "",
             "Reply 3.1": ""},
        "Question 2":
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

    enemy_lines_dictionary = {
        "Level 1": [slime_chat, pixie_chat, wolf_chat, skeleton_chat, ghost_chat, golem_chat],
        "Level 2": [spider_chat, archer_chat, spirit_chat, succubus_chat, maid_chat, gargoyle_chat],
        "Miniboss": [cerberus_chat, oberon_chat, dracula_chat],
        "Final Boss": dragon_chat}

    return enemy_lines_dictionary
