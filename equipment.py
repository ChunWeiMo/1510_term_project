"""
equipment module
"""
character_stats = {"Level": 1, "HP": 100, "STR": 1,
                   "DEF": 1, "CHR": 1, "SPD": 1, "LUK": 1, "VIS": 3}
level1_equipment = {1: ["Steel sword", character_stats["STR"]+3],
                    2: ["Small round shield", character_stats["DEF"]+3],
                    3: ["Cloak", character_stats["SPD"]+3],
                    4: ["Cheat coin", character_stats["LUK"]+3],
                    5: ["Noble Insignia", character_stats["CHR"]+3],
                    6: ["The lance of curses", character_stats["STR"]+6, character_stats["HP"]-30],
                    7: ["Angel's winged garment", character_stats["SPD"]+6, character_stats["DEF"]-2],
                    8: ["Heavy knight's armor", character_stats["DEF"]+6, character_stats["SPD"]-2],
                    9: ["Beginner adventurer's guide", character_stats["STR"]+1, character_stats["DEF"]+1, character_stats["CHR"]+1, character_stats["SPD"]+1],
                    10: ["Single-barrel telescope", character_stats["VIS"]+1],
                    11: ["Giant hammer", character_stats["STR"]+5, character_stats["SPD"]-1]
                        }

level2_equipment = {1: ["Silver sword", character_stats["STR"]+7],
                    2: ["Hero's spear", character_stats["STR"]+5, character_stats["SPD"]+2],
                    3: ["Hermes shoes", character_stats["SPD"]+7],
                    4: ["King's scepter", character_stats["STR"]+1, character_stats["CHR"]+6],
                    5: ["Kiss of Rose Princess", character_stats["CHR"]+7],
                    6: ["Platinum shield", character_stats["DEF"]+7],
                    7: ["Oracle crystal ball", character_stats["VIS"]+2],
                    8: ["Luxurious carriage", character_stats["SPD"]+3, character_stats["CHR"]+4],
                    9: ["Spirits guardian", character_stats["DEF"]+3, character_stats["SPD"]+3],
                    
}

level3_equipment = {1: ["Ragnarök", character_stats["STR"]+15],
                    2: ["The Goddess's blessing", character_stats["DEF"]+15],
                    3: ["Garuda's wing", character_stats["SPD"]+15],
                    4: ["Dragon slayer", character_stats["STR"]+10, character_stats["SPD"]+5]
                    }
