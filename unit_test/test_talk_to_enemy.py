import unittest
from unittest import TestCase
from unittest.mock import patch
from modules.battle.talk import talk_to_enemy


class TestTalkToEnemy(TestCase):
    def test_enemy_is_miniboss(self):
        with unittest.mock.patch('modules.battle.talk.talk_boss') as mock_talk_boss:
            character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                         "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                    "Items": {"Gold": 0, "Potions": 0}}
            enemy_appeared = {"Name": "Cerberus", "HP": 50, "STR": 5, "DEF": 5, "SPD": 0, "EXP": 8, "Gold": 5}
            specific_enemy_lines = {
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
                     "Reply 1.1": "I'm not thaaat old, but I guess you can say my wealth of knowledge is comparable "
                                  "to someone"
                                  "that old.",
                     "Reply 2": "Under 100, you think I'm a minor?! You know, when you go too young it's also an "
                                "insult right?",
                     "Reply 2.1": "I may be beautiful but I'm not that young good sir.",
                     "Reply 3": "Don't try to dodge the question!",
                     "Reply 3.1": "Playing it safe huh, aren't you a careful hero."}}
            turn = 1
            max_turn = 3
            talk_to_enemy(character_dictionary, enemy_appeared)
            mock_talk_boss.assert_called_with(specific_enemy_lines, enemy_appeared, character_dictionary, turn,
                                              max_turn)

    def test_enemy_is_final_boss(self):
        with unittest.mock.patch('modules.battle.talk.talk_boss') as mock_talk_boss:
            character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                         "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                    "Items": {"Gold": 0, "Potions": 0}}
            enemy_appeared = {"Name": "Evil Dragon", "HP": 100, "STR": 7, "DEF": 4, "SPD": 3, "EXP": 10, "Gold": 10}
            specific_enemy_lines = {
                "Question 1":
                    {"Question": "*Yawn* I just woke up, what's this puny human doing here?",
                     "Answer 1": "I want to talk.",
                     "Answer 2": "I want you to leave.",
                     "Answer 3": "I'm here to kill you.",
                     "Reply 1": "I am hungry right now!! I don't have the patience to talk to you puny human.",
                     "Reply 1.1": "Hmph, I was just about to go eat some townsfolk.",
                     "Reply 2": "I wake up to an intruder in my home and the first thing he says is to leave?!!?!",
                     "Reply 2.1": "Hmm, not interested.",
                     "Reply 3": "I accept your duel!",
                     "Reply 3.1": "Ok, but you clearly have not yet. So what is it?"},
                "Question 2":
                    {"Question": "Well, is there anything else you want to say to me?",
                     "Answer 1": "I know dragons like shiny things. What if I gave you all my gold?\nWill that "
                                 "placate you?",
                     "Answer 2": "Please don't kill the townspeople!",
                     "Answer 3": "I will protect this town.",
                     "Reply 1": "How greedy do you think I am?!",
                     "Reply 1.1": "Hmph, it is not enough, but I will at least hear you out.",
                     "Reply 2": "I don't take orders from you!",
                     "Reply 2.1": "Hmph, I will give you a chance plead your case.\nOnly because I'm still waking up.",
                     "Reply 3": "I hate selfless heroes like you!",
                     "Reply 3.1": "Why is it so important to you?"},
                "Question 3":
                    {"Question": "Why do you insist on protecting them?",
                     "Answer 1": "They cannot be held accountable for what happened 500 years ago.",
                     "Answer 2": "This is what I was hired to do.",
                     "Answer 3": "This goes against my morals as a hero!",
                     "Reply 1": "You are right. Then you will have to be the outlet for my rage!",
                     "Reply 1.1": "What you say is reasonable.",
                     "Reply 2": "You should learn to take jobs closer to your skill level then!",
                     "Reply 2.1": "Acting like you don't care huh? Who is the gold hoarder now?",
                     "Reply 3": "Heroes, you all have so much pride.\nIt makes me want to kill you!",
                     "Reply 3.1": "Hah! Morals huh."},
                "Question 4":
                    {"Question": "If I refuse will you kill me?",
                     "Answer 1": "I'm sure we can come to an understanding.",
                     "Answer 2": "Yes.",
                     "Answer 3": "You will leave me no choice.",
                     "Reply 1": "So naive...Let me show you the real world!",
                     "Reply 1.1": "I've never met such a stubborn hero before.",
                     "Reply 2": "Ok, try it then!",
                     "Reply 2.1": "Hah! I like your resolve.",
                     "Reply 3": "The choice is not yours to make hero.\nMind your position.",
                     "Reply 3.1": "Hmm. Well then."},
                "Question 5":
                    {"Question": "So then what do you propose?",
                     "Answer 1": "Let's live in peace.",
                     "Answer 2": "Let's go travelling together!",
                     "Answer 3": "Why don't you go back to sleep...",
                     "Reply 1": "How is that possible! I need to consume flesh to survive!",
                     "Reply 1.1": "If the villagers promise not to send heroes after me anymore.",
                     "Reply 2": "Are you insane!",
                     "Reply 2.1": "Well, that doesn't sound so bad actually.\nThe world must have changed a lot in "
                                  "500 years.",
                     "Reply 3": "I just woke up from my curse and you want to curse me again!!",
                     "Reply 3.1": "Ugh you know what, I don't want to deal with you anymore.\nMaybe I will."}}
            turn = 1
            max_turn = 5
            talk_to_enemy(character_dictionary, enemy_appeared)
            mock_talk_boss.assert_called_with(specific_enemy_lines, enemy_appeared, character_dictionary, turn,
                                              max_turn)

    @patch('builtins.input', side_effect=[1])
    @patch('modules.battle.enemy.random.randint', return_value=1)
    def test_enemy_is_regular_enemy(self, _, __):
        with unittest.mock.patch('modules.battle.talk.randomizer') as mock_randomizer:
            character_dictionary = {"Character_status": {"Level": 1, "HP": 100, "STR": 1,
                                                         "DEF": 5, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}, "EXP": 0,
                                    "Items": {"Gold": 0, "Potions": 0}}
            enemy_appeared = {"Name": "Slime", "HP": 10, "STR": 2, "DEF": 1, "SPD": 2, "EXP": 3, "Gold": 1}
            specific_enemy_lines = {
                "Question": "Plip plop plip plop~~",
                "Answer 1": "*Pat it*",
                "Answer 2": "*Squeeze it*",
                "Answer 3": "*kick it*",
                "Reply 1": "Pliippp! (it looks happy)",
                "Reply 2": "PLIPP! (battle)",
                "Reply 2.1": "Pliiiipppp~ (it looks content)",
                "Reply 3": "GRRrr (battle)",
                "Reply 3.1": "plip..(it looks sad and scared)"}
            talk_to_enemy(character_dictionary, enemy_appeared)
            mock_randomizer.assert_called_with(specific_enemy_lines)
