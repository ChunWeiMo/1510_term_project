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
        "Answer 1": "Sure...(-5 HP)",
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
        "Question": "Never should have come here.",
        "Answer 1": "Yeah...I'll just leave now.",
        "Answer 2": "Why? What's over here?",
        "Answer 3": "YOU never should have lived here!",
        "Reply 1": "Thanks...",
        "Reply 2": "Why do you wanna know!!!",
        "Reply 2.1": "Nothing really, just my house.",
        "Reply 3": "You trespass, then try to kick me out???!",
        "Reply 3.1": "Uh, my bad...please don't kill me."}
    archer_chat = {
        "Question": "Can I have some gold?",
        "Answer 1": "Ok, if you leave me alone (-10 Gold)",
        "Answer 2": "No way, bony.",
        "Answer 3": "You should be giving ME gold!",
        "Reply 1": "Hehe, thanks~",
        "Reply 1.1": "You don't have any don't lie to me!!!",
        "Reply 2": "I'll turn you into bones too!!",
        "Reply 2.1": "Uhh, ok then.",
        "Reply 3": "I don't have any! Why do you think I'm asking you??",
        "Reply 3.1": "EEEK! Yessir! (+5 Gold)"}
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
        "Answer 1": "Sure ♥(-5 HP)",
        "Answer 2": "Ok, but buy me coffee first!",
        "Answer 3": "No thanks!",
        "Reply 1": "Such a lovely and tasty adventurer~♥",
        "Reply 2": "Are you crazy??",
        "Reply 2.1": "How's a potion sound?",
        "Reply 3": "WHY NOOOOTTT!!!",
        "Reply 3.1": "Aww ok...I don't get many adventurers around here..."}
    maid_chat = {
        "Question": "Good afternoon adventurer! What brings you here?",
        "Answer 1": "I'm here to slay the dragon.",
        "Answer 2": "I'd like a cup of tea.",
        "Answer 3": "Have you been cleaning? This dungeon is still so dirty...",
        "Reply 1": "Why, I'm sure you can't but feel free to try sir.",
        "Reply 2": "What makes you think I'd serve you?",
        "Reply 2.1": "I don't have any human food or drinks, but I have this potion I got from a dead adventurer!",
        "Reply 3": "How dare you sir!",
        "Reply 3.1": "Well...My master dragon has been sleeping~"}
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
            {"Question": "Why does cerberus have 3 heads?",
             "Answer 1": "Because it makes you 3 times smarter!",
             "Answer 2": "So you can eat 3 times as much!",
             "Answer 3": "Because you are lonely?",
             "Reply 1": "Don't think you can flatter me!",
             "Reply 1.1": "Aw shucks...",
             "Reply 2": "Are you saying I'm fat??? I can also eat you 3 times as fast!",
             "Reply 2.1": "Well I do love cheeseburgers...",
             "Reply 3": "We're not lonely!",
             "Reply 3.1": "Well, you can stay here with us if you're lonely too."},
        "Question 2":
            {"Question": "What is cerberus' favourite food?",
             "Answer 1": "Human flesh.",
             "Answer 2": "Cheeseburgers.",
             "Answer 3": "Kibbles 'N Bits!",
             "Reply 1": "SO TRUE!!!",
             "Reply 1.1": "Hehe, no it's cheeseburgers...flesh is second favourite.",
             "Reply 2": "You're not wrong but it makes me angry that you knew!!!",
             "Reply 2.1": "Yeah, did you bring any with you by any chance?",
             "Reply 3": "SO DEGRADING!!",
             "Reply 3.1": "Woof! Woof!"},
        "Question 3":
            {"Question": "How old do you think cerberus is?",
             "Answer 1": "You look very wise and knowledgeable so you must be over 500!",
             "Answer 2": "Your fur is so shiny and thick, you must be under 100!",
             "Answer 3": "It is hard to tell since you are so well kept and majestic looking.",
             "Reply 1": "So basically you think I look old!!",
             "Reply 1.1": "I'm not thaaat old, but I guess you can say my wealth of knowledge is comparable to someone"
                          "that old.",
             "Reply 2": "Under 100, you think I'm a minor?! You know, when you go too young it's also an insult right?",
             "Reply 2.1": "I may be beautiful but I'm not that young good sir.",
             "Reply 3": "Don't try to dodge the question!",
             "Reply 3.1": "Playing it safe huh, aren't you a careful hero."}}

    oberon_chat = {
        "Question 1":
            {"Question": "Oho, you want to talk?\nWell first of all, I have to ask...\nDo you know where my wife is?",
             "Answer 1": "I don't know.",
             "Answer 2": "She's just around the corner...",
             "Answer 3": "Probably dead somewhere.",
             "Reply 1": "Curb your disrespectful tone.",
             "Reply 1.1": "Phew, time to relax for a bit.",
             "Reply 2": "AHHHHH...don't scare me like that.",
             "Reply 2.1": "Oh really? I have nothing to hide...today.",
             "Reply 3": "SHUT UP HUMAN. This is not a joke.",
             "Reply 3.1": "Haha don't say that...if she finds out I'm dead meat."},
        "Question 2":
            {"Question": "Well, anyways, now that that is out of the way...\nHave you seen any cute girls around?",
             "Answer 1": "Yeah, you are looking at her~",
             "Answer 2": "There is a succubus in the dungeon.",
             "Answer 3": "I am going to report you to Titania.",
             "Reply 1": "Absolutely not my type!!!",
             "Reply 1.1": "Erm, heroes are not quite my taste.",
             "Reply 2": "I won't be fooled by her like you!",
             "Reply 2.1": "Eh, been there, done that.",
             "Reply 3": "Not if I kill you first!",
             "Reply 3.1": "Please don't! I won't do it again..."},
        "Question 3":
            {"Question": "Hmph, you've managed to convince me so far.\n I guess I should get a bit more serious.\n"
                         "You must have murdered many of my children to get here.",
             "Answer 1": "No! I swear I ran away or talked to any Pixie I've encountered!",
             "Answer 2": "Only the evil ones!",
             "Answer 3": "Certainly not, we only danced and drank wine together.",
             "Reply 1": "You think I can trust the words of a human?!",
             "Reply 1.1": "I'm glad to hear that my children are safe.",
             "Reply 2": "Who are you to judge my children!",
             "Reply 2.1": "There are no evil faeries! Mischievous perhaps, but not evil.",
             "Reply 3": "You had a party without me?! Preposterous!",
             "Reply 3.1": "I'm glad you had fun with my little ones."}}

    dracula_chat = {
        "Question 1":
            {"Question": "You wish to speak to me?!\nProve your worth. Let me taste your blood.",
             "Answer 1": "Hmmm if it is the only way. (HP -20)",
             "Answer 2": "I am weak please spare me!",
             "Answer 3": "My blood tastes awful though...",
             "Reply 1": "Blergh! tastes awful",
             "Reply 1.1": "Hmm, not bad.",
             "Reply 2": "I will spare you from this world!",
             "Reply 2.1": "Hmph, I have no need for weakling blood anyways.",
             "Reply 3": "I will be the one to decide that!",
             "Reply 3.1": "True, you don't look particularly appetizing."},
        "Question 2":
            {"Question": "Anyways, what is it you want to say to me?",
             "Answer 1": "Please make me immortal!",
             "Answer 2": "I'm here to kill the dragon. Any advice?",
             "Answer 3": "You are my idol!",
             "Reply 1": "Hah! You think you deserve to live forever?",
             "Reply 1.1": "Don't be fooled, it is but a curse.",
             "Reply 2": "Not if I kill you first!",
             "Reply 2.1": "Well, you better hurry up while he's still sleeping. Then I can take over this dump.",
             "Reply 3": "You are insane.",
             "Reply 3.1": "Well, a little praise never hurt anyone."},
        "Question 3":
            {"Question": "Now you must be satisfied to be able to speak with me.\nLet me ask you a final question.\n"
                         "Do you think humans and vampires can coexist?",
             "Answer 1": "",
             "Answer 2": "",
             "Answer 3": "",
             "Reply 1": "",
             "Reply 1.1": "",
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
             "Reply 1.1": "",
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
             "Reply 1.1": "",
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
             "Reply 1.1": "",
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
             "Reply 1.1": "",
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
             "Reply 1.1": "",
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
