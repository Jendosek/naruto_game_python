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
        os.system("cls" if os.name == "nt" else "clear")

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
        bar_len = 10

        def bar(value, max_val=20):
            filled = int(value / max_val * bar_len)
            return "█" * filled + "░" * (bar_len - filled)

        print(f"\n{Display.YELLOW}╔{'═' * 32}╗")
        print(f"║  {Display.BOLD}{character.name} — Стати{Display.RESET}{Display.YELLOW}{'':>12}║")
        print(f"╠{'═' * 32}╣{Display.RESET}")
        print(f"{Display.YELLOW}║{Display.RESET}  Ніндзюцу:  {Display.RED}{bar(character.ninjutsu)}{Display.RESET} {character.ninjutsu:>2}  {Display.YELLOW}║{Display.RESET}")
        print(f"{Display.YELLOW}║{Display.RESET}  Гендзюцу:  {Display.MAGENTA}{bar(character.genjutsu)}{Display.RESET} {character.genjutsu:>2}  {Display.YELLOW}║{Display.RESET}")
        print(f"{Display.YELLOW}║{Display.RESET}  Інтелект:  {Display.CYAN}{bar(character.intelligence)}{Display.RESET} {character.intelligence:>2}  {Display.YELLOW}║{Display.RESET}")
        print(f"{Display.YELLOW}║{Display.RESET}  Рішучість: {Display.GREEN}{bar(character.resolve)}{Display.RESET} {character.resolve:>2}  {Display.YELLOW}║{Display.RESET}")
        print(f"{Display.YELLOW}╠{'═' * 32}╣")
        print(f"║  Сила: {character.get_power_level()}{'':<24}║")
        print(f"╚{'═' * 32}╝{Display.RESET}\n")

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