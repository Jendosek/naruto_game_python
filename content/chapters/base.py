from abc import ABC, abstractmethod
from engine.character import Character
from engine.combat import CombatSystem
from engine.minigames import MiniGames
from engine.display import Display


class Chapter(ABC):

    def __init__(
        self,
        character: Character,
        combat: CombatSystem,
        minigames: MiniGames,
        display: Display,
    ):
        self.character = character
        self.combat = combat
        self.minigames = minigames
        self.display = display

    def play(self):
        self.intro()
        self.gameplay()
        self.finale()

    @abstractmethod
    def intro(self):
        pass

    @abstractmethod
    def gameplay(self):
        pass

    @abstractmethod
    def finale(self):
        pass