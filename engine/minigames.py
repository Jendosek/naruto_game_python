import random
import time
import sys
import threading
from engine.display import Display


class MiniGames:

    @staticmethod
    def sequence_memory(length, symbols = None):
        if symbols is None:
            symbols = ["☆", "✦", "◈", "⬡", "△", "○", "□"]

        sequence = [random.choice(symbols) for _ in range(length)]

        print(f"\n  {Display.CYAN}Запам'ятай послідовність!{Display.RESET}")
        time.sleep(1)

        print(f"\n  {Display.BOLD}", end="")
        for s in sequence:
            print(f" {s} ", end="")
            sys.stdout.flush()
            time.sleep(0.6)
        print(Display.RESET, end="")
        sys.stdout.flush()

        time.sleep(1.5)

        print(f"\r\033[2K  {Display.DIM}Послідовність зникла...{Display.RESET}\n")
        time.sleep(0.5)


        unique = list(set(sequence))
        random.shuffle(unique)

        extras = [s for s in symbols if s not in unique]
        if extras:
            unique.extend(random.sample(extras, min(2, len(extras))))
        random.shuffle(unique)

        print(f"  Символи: {' '.join(f'[{i+1}]{s}' for i, s in enumerate(unique))}")
        print(f"  {Display.DIM}Введи {length} номерів через пробіл:{Display.RESET}")

        try:
            raw = input("  > ").strip().split()
            correct = 0
            for i, num_str in enumerate(raw[:length]):
                idx = int(num_str) - 1
                if 0 <= idx < len(unique) and i < len(sequence) and unique[idx] == sequence[i]:
                    correct += 1
        except (ValueError, IndexError):
            correct = 0

        if correct == length:
            print(f"\n  {Display.GREEN}Ідеально! Всі {length} правильно.{Display.RESET}")
        elif correct > 0:
            print(f"\n  {Display.YELLOW}{correct}/{length} правильно.{Display.RESET}")
        else:
            print(f"\n  {Display.RED}Жодного правильного...{Display.RESET}")

        return correct

    @staticmethod
    def stealth_run(difficulty, grid_size = 5):
        directions = ["ліво", "прямо", "право"]

        patrols = []
        for _ in range(grid_size):
            if random.random() < difficulty / grid_size:
                patrols.append(random.choice(directions))
            else:
                patrols.append(None)

        print(f"\n  {Display.CYAN}Стелс-місія. {grid_size} кроків до цілі.{Display.RESET}")
        print(f"  {Display.DIM}На кожному кроці вибери напрямок. Уникай патрулів.{Display.RESET}\n")

        detected = False
        for step in range(grid_size):
            print(f"  {Display.YELLOW}Крок {step + 1}/{grid_size}{Display.RESET}")

            # Іноді даємо підказку
            if patrols[step] and random.random() < 0.4:
                other_dirs = [d for d in directions if d != patrols[step]]
                hint_dir = random.choice(other_dirs)
                print(f"  {Display.DIM}(Чутно шум з одного боку...){Display.RESET}")

            idx = Display.choice(["← Ліво", "↑ Прямо", "→ Право"])
            chosen = directions[idx]

            if patrols[step] and chosen == patrols[step]:
                print(f"  {Display.RED}! Патруль помітив тебе!{Display.RESET}")
                detected = True
                break
            else:
                print(f"  {Display.GREEN}Чисто.{Display.RESET}")
            time.sleep(0.3)

        if not detected:
            print(f"\n  {Display.GREEN}Пройшов як тінь. Непомічений.{Display.RESET}")
            return True
        else:
            print(f"\n  {Display.RED}Виявлений. Місію ускладнено.{Display.RESET}")
            return False

    @staticmethod
    def quick_choice(question, options, time_limit = 0):
        print(f"\n  {Display.BOLD}{question}{Display.RESET}")

        if time_limit > 0:
            print(f"  {Display.RED}У тебе {time_limit} секунд!{Display.RESET}")

            result = [None]

            def get_input():
                result[0] = Display.choice(options)

            thread = threading.Thread(target=get_input, daemon=True)
            thread.start()
            thread.join(timeout=time_limit)

            if result[0] is None:
                chosen = random.randint(0, len(options) - 1)
                print(f"\n  {Display.RED}Час вийшов! Вибрано автоматично: {options[chosen]}{Display.RESET}")
                return chosen
            return result[0]
        else:
            return Display.choice(options)