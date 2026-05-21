from content.chapters.base import Chapter
from content.dialogues import CHAPTER_1


class Chapter1(Chapter):
    def intro(self):
        self.display.chapter_title("РОЗДІЛ 1: ТІ, ХТО БАЧАТЬ ДАЛІ")
        self.display.narrate(CHAPTER_1["intro"], delay=0.03)
        self.display.dialogue("Шісуі", CHAPTER_1["shisui_talk"])

    def gameplay(self):
        self.display.narrate(CHAPTER_1["gameplay_intro"])

        score = self.minigames.sequence_memory(5)

        if score >= 4:
            self.display.narrate(CHAPTER_1["minigame_win"])
            self.character.boost("intelligence", 3)
            self.character.boost("ninjutsu", 1)
        else:
            self.display.narrate(CHAPTER_1["minigame_fail"])
            self.character.boost("intelligence", 1)

    def finale(self):
        self.display.narrate(CHAPTER_1["finale_intro"])

        choice_1 = self.minigames.quick_choice(
            CHAPTER_1["anbu_q1"],
            CHAPTER_1["anbu_a1"]
        )

        if choice_1 == 0:
            self.character.boost("resolve", 2)
        elif choice_1 == 1:
            self.character.boost("resolve", -1)
            self.character.boost("genjutsu", 1)
        elif choice_1 == 2:
            self.character.boost("intelligence", 2)
            self.character.boost("ninjutsu", 2)

        choice_2 = self.minigames.quick_choice(
            CHAPTER_1["anbu_q2"],
            CHAPTER_1["anbu_a2"]
        )

        if choice_2 == 0:
            self.character.boost("intelligence", 1)
        elif choice_2 == 1:  # Розмова
            self.character.boost("genjutsu", 2)
        elif choice_2 == 2:  # Ліквідація (Шлях темряви)
            self.character.boost("resolve", 3)
            self.character.boost("ninjutsu", 2)

        self.display.narrate(CHAPTER_1["finale_outro"])