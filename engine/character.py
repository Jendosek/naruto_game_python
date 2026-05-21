class Character:
    def __init__(self, name: str = "Itachi"):
        self.name = name
        self.ninjutsu = 5
        self.genjutsu = 5
        self.intelligence = 5
        self.resolve = 5
        self.hp = 100

    def boost(self, stat: str, amount: int) -> None:
        pass

    def get_power_level(self) -> int:
        pass

    def is_weak(self) -> bool:
        pass

    def is_strong(self) -> bool:
        pass

    def reset_hp(self) -> None:
        pass