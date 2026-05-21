import random
import time
from abc import ABC, abstractmethod
from engine.character import Character
from engine.display import Display


class AttackStrategy(ABC):

    name: str = "Attack"
    description: str = ""

    @abstractmethod
    def execute(self, attacker, defender):
        pass


class TaijutsuAttack(AttackStrategy):

    name = "Тайдзюцу"
    description = "Фізичний удар кунаєм"

    def execute(self, attacker, defender):
        base_damage = attacker.ninjutsu * 2 + random.randint(-2, 3)
        damage = max(1, base_damage)
        return {"damage": damage, "message": "Швидкий удар кунаєм!"}


class GenjutsuAttack(AttackStrategy):
    name = "Гендзюцу"
    description = "Пастка ілюзій"

    def execute(self, attacker, defender):
        base_damage = attacker.genjutsu * 3 + random.randint(-3, 4)
        damage = max(1, base_damage)
        if defender.get("weakness") == "genjutsu":
            damage = int(damage * 1.5)
            return {"damage": damage, "message": "Гендзюцу... Ворог повністю в ілюзії! Критичний удар!"}
        return {"damage": damage, "message": "Шарінган активовано. Ворог бачить те, чого немає."}


class ShurikenAttack(AttackStrategy):

    name = "Шурікендзюцу"
    description = "Шурікени з тіні"

    def execute(self, attacker, defender):
        base_damage = attacker.ninjutsu + attacker.intelligence + random.randint(-2, 2)
        damage = max(1, base_damage)
        return {"damage": damage, "message": "Шурікени летять з мертвої зони!"}


class TsukuyomiAttack(AttackStrategy):
    name = "Цукуйомі"
    description = "Абсолютна ілюзія Мангек'ю Шарінгану"

    def execute(self, attacker, defender):
        damage = attacker.genjutsu * 5
        attacker.hp -= 15
        return {
            "damage": damage,
            "message": "М А Н Г Е К ' Ю   Ш А Р І Н Г А Н: Ц У К У Й О М І !\n"
                       "  72 години... в одну секунду.",
        }


class CombatSystem:

    def run_battle(
        self,
        player: Character,
        enemy: dict,
        available_attacks: list[AttackStrategy],
        show_hints: bool = False,
    ) -> bool:
        display = Display()

        player.reset_hp()
        enemy_hp = enemy["hp"]
        enemy_atk = enemy.get("attack", 8)
        enemy_name = enemy["name"]

        display.separator()
        display.narrate(f"⚔  Бій: {player.name} vs {enemy_name}  ⚔")
        print()

        if show_hints and player.intelligence >= 8 and enemy.get("weakness"):
            print(f"  {Display.CYAN}[Шарінган бачить]: слабкість ворога — {enemy['weakness']}{Display.RESET}\n")

        turn = 1
        while player.hp > 0 and enemy_hp > 0:

            print(f"  {Display.GREEN}{player.name}: {player.hp} HP{Display.RESET}  |  "
                  f"{Display.RED}{enemy_name}: {enemy_hp} HP{Display.RESET}")
            print(f"  {Display.DIM}--- Хід {turn} ---{Display.RESET}")


            attack_options = [f"{a.name} — {a.description}" for a in available_attacks]
            idx = display.choice(attack_options)
            attack = available_attacks[idx]


            result = attack.execute(player, enemy)
            enemy_hp -= result["damage"]
            print(f"\n  {Display.YELLOW}► {result['message']}{Display.RESET}")
            print(f"    Урон: {Display.RED}{result['damage']}{Display.RESET}")
            time.sleep(0.8)

            if enemy_hp <= 0:
                break


            enemy_damage = enemy_atk + random.randint(-3, 3)
            enemy_damage = max(1, enemy_damage)
            player.hp -= enemy_damage
            print(f"\n  {Display.RED}◄ {enemy_name} атакує! Урон: {enemy_damage}{Display.RESET}")
            time.sleep(0.5)
            print()

            turn += 1


        display.separator()
        if player.hp > 0:
            display.narrate(f"✦ {enemy_name} повалений.")
            return True
        else:
            display.narrate(f"...{player.name} падає на коліна.")
            return False