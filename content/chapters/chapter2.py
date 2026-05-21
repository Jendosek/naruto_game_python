from content.chapters.base import Chapter
from content.dialogues import CHAPTER_2
from engine.combat import TaijutsuAttack, GenjutsuAttack, ShurikenAttack

class Chapter2(Chapter):
    def intro(self):
        self.display.chapter_title("РОЗДІЛ 2: ТІНІ")
        self.display.narrate(CHAPTER_2["intro"], delay=0.04)

    def gameplay(self):
        self.display.narrate(CHAPTER_2["stealth_intro"])

        base_difficulty = 10
        stealth_difficulty = max(2, base_difficulty - self.character.intelligence)

        is_stealth_successful = self.minigames.stealth_run(stealth_difficulty)

        if is_stealth_successful:
            self.display.narrate(CHAPTER_2["stealth_success"])
            self.character.boost("resolve", 2)
        else:
            self.display.narrate(CHAPTER_2["stealth_fail"])
            self.character.hp -= 15
            self.character.boost("resolve", -1)

        self.display.narrate(CHAPTER_2["combat_intro"])
        enemy_data = {"name": "Учіха Яшіро", "hp": 50, "damage": 10}

        battle_won = self.combat.run_battle(
            player=self.character,
            enemy=enemy_data,
            available_attacks=[TaijutsuAttack(), GenjutsuAttack(), ShurikenAttack()]
        )

        if battle_won:
            self.display.narrate(CHAPTER_2["combat_win"])
            self.character.boost("ninjutsu", 2)
        else:
            self.display.narrate(CHAPTER_2["combat_fail"])
            self.character.hp -= 20

    def finale(self):
        self.display.narrate(CHAPTER_2["finale_intro"], delay=0.05)

        if self.character.resolve >= 10:
            self.display.dialogue("Ітачі", CHAPTER_2["itachi_high_resolve"])
        else:
            self.display.dialogue("Ітачі", CHAPTER_2["itachi_low_resolve"])

        self.character.boost("genjutsu", 3)