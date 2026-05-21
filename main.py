from engine.character import Character
from engine.combat import CombatSystem
from engine.minigames import MiniGames
from engine.display import Display
from content.chapters.chapter1 import Chapter1
from content.chapters.chapter2 import Chapter2
from content.chapters.chapter3 import Chapter3


def main():
    display = Display()
    display.clear()

    display.chapter_title("ITACHI: PATH OF SACRIFICE")
    display.narrate("Шлях шінобі — це шлях жертв.")
    display.narrate("Кожен вибір наближає тебе до долі...")
    display.pause()

    character = Character()
    combat = CombatSystem()
    minigames = MiniGames()

    chapters = [
        Chapter1(character, combat, minigames, display),
        Chapter2(character, combat, minigames, display),
        Chapter3(character, combat, minigames, display),
    ]

    for i, chapter in enumerate(chapters):
        display.clear()
        chapter.play()
        display.show_stats(character)
        if i < len(chapters) - 1:
            display.pause("Натисни Enter для наступної глави...")

    # Фінал
    display.separator()
    if character.is_strong():
        display.narrate("Ворон полетів у бік Конохи. Повідомлення доставлено.")
        display.narrate("Ітачі посміхнувся в останнє.")
    else:
        display.narrate("...Він впав. Але навіть у падінні — захищав.")

    display.narrate("\n「 Кожна людина живе, покладаючись на свої знання та уявлення,")
    display.narrate("  і це називає реальністю. Але знання та розуміння — речі неоднозначні.")
    display.narrate("  Ця реальність може бути ілюзією. 」")
    display.narrate(f"\n  — Учіха Ітачі")
    print()


if __name__ == "__main__":
    main()