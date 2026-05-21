from content.chapters.base import Chapter
from content.dialogues import CHAPTER_3
from engine.combat import TaijutsuAttack, ShurikenAttack, GenjutsuAttack, TsukuyomiAttack

class Chapter3(Chapter):
    def intro(self):
        self.display.chapter_title("РОЗДІЛ 3: ОСТАННЄ ГЕНДЗЮЦУ")
        self.display.narrate(CHAPTER_3["intro"], delay=0.04)
        self.display.dialogue("Саске", CHAPTER_3["sasuke_talk"])
        self.display.dialogue("Ітачі", CHAPTER_3["itachi_reply"])

    def gameplay(self):
        self.display.narrate(CHAPTER_3["combat_intro"])

        available_attacks = [TaijutsuAttack(), ShurikenAttack(), GenjutsuAttack()]

        if self.character.genjutsu >= 15:
            self.display.narrate(CHAPTER_3["tsukuyomi_unlocked"])
            available_attacks.append(TsukuyomiAttack())

        enemy_data = {"name": "Учіха Саске", "hp": 200, "damage": 20}

        battle_won = self.combat.run_battle(
            player=self.character,
            enemy=enemy_data,
            available_attacks=available_attacks
        )

        if battle_won:
            self.display.narrate(CHAPTER_3["combat_survived"])
        else:
            self.display.narrate(CHAPTER_3["combat_failed"])

    def finale(self):
        self.display.narrate(CHAPTER_3["finale_intro"], delay=0.05)
        self.display.narrate(CHAPTER_3["the_poke"], delay=0.07)
        self.display.narrate(CHAPTER_3["death"], delay=0.04)

        if self.character.get_power_level() >= 35:
            self.display.narrate(CHAPTER_3["secret_ending"], delay=0.06)