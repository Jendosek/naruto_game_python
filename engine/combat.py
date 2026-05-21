from abc import ABC, abstractmethod
from engine.character import Character


class AttackStrategy(ABC):

    name: str = "Attack"
    description: str = ""

    @abstractmethod
    def execute(self, attacker: Character, defender: dict) -> dict:
        pass


class TaijutsuAttack(AttackStrategy):

    name = "Тайдзюцу"
    description = "Фізичний удар кунаєм"

    def execute(self, attacker: Character, defender: dict) -> dict:
        pass


class GenjutsuAttack(AttackStrategy):

    name = "Гендзюцу"
    description = "Пастка ілюзій"

    def execute(self, attacker: Character, defender: dict) -> dict:
        pass


class ShurikenAttack(AttackStrategy):

    name = "Шурікендзюцу"
    description = "Шурікени з тіні"

    def execute(self, attacker: Character, defender: dict) -> dict:
        pass


class TsukuyomiAttack(AttackStrategy):

    name = "Цукуйомі"
    description = "Абсолютна ілюзія Мангек'ю Шарінгану"

    def execute(self, attacker: Character, defender: dict) -> dict:
        pass


class CombatSystem:

    def run_battle(
        self,
        player: Character,
        enemy: dict,
        available_attacks: list[AttackStrategy],
        show_hints: bool = False,
    ) -> bool:
        pass