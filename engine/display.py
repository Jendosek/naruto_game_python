import sys
import time
import os


class Display:
    
    # Кольори ANSI
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"

    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear 2>/dev/null")

    @staticmethod
    def narrate(text: str, delay: float = 0.03) -> None:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    @staticmethod
    def dialogue(speaker: str, text: str) -> None:
        print(f"\n{Display.CYAN}[{speaker}]{Display.RESET}: {text}")
        time.sleep(0.5)

    @staticmethod
    def show_stats(character) -> None:
        print(f"\n  {character.name} — Стати")
        print(f"  Ніндзюцу:  {'█' * character.ninjutsu}{'░' * (20 - character.ninjutsu)} {character.ninjutsu}/20")
        print(f"  Гендзюцу:  {'█' * character.genjutsu}{'░' * (20 - character.genjutsu)} {character.genjutsu}/20")
        print(
            f"  Інтелект:  {'█' * character.intelligence}{'░' * (20 - character.intelligence)} {character.intelligence}/20")
        print(f"  Рішучість: {'█' * character.resolve}{'░' * (20 - character.resolve)} {character.resolve}/20")
        print(f"  Сила: {character.get_power_level()}\n")

    @staticmethod
    def chapter_title(title: str) -> None:
        width = len(title) + 8
        print(f"\n{Display.RED}{Display.BOLD}")
        print(f"{'─' * width}")
        print(f"    {title}")
        print(f"{'─' * width}")
        print(f"{Display.RESET}\n")
        time.sleep(1)

    @staticmethod
    def choice(options: list[str]) -> int:
        print()
        for i, option in enumerate(options, 1):
            print(f"  {Display.YELLOW}[{i}]{Display.RESET} {option}")
        print()

        while True:
            try:
                raw = input(f"{Display.DIM}Твій вибір > {Display.RESET}")
                idx = int(raw) - 1
                if 0 <= idx < len(options):
                    return idx
                print(f"  Введи число від 1 до {len(options)}")
            except ValueError:
                print(f"  Введи число від 1 до {len(options)}")

    @staticmethod
    def separator() -> None:
        print(f"\n{Display.DIM}{'─' * 40}{Display.RESET}\n")

    @staticmethod
    def pause(message: str = "Натисни Enter щоб продовжити...") -> None:
        input(f"\n{Display.DIM}{message}{Display.RESET}")