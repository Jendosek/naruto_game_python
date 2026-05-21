class Character:
    VALID_STATS = ("ninjutsu", "genjutsu", "intelligence", "resolve")
    MAX_STAT = 20

    def __init__(self, name: str = "Itachi"):
        self.name = name
        self.ninjutsu = 5
        self.genjutsu = 5
        self.intelligence = 5
        self.resolve = 5
        self.hp = 100

    def boost(self, stat: str, amount: int) -> None:
        if stat not in self.VALID_STATS:
            raise AttributeError(f"Невідомий стат: {stat}. Доступні: {self.VALID_STATS}")
        current = getattr(self, stat)
        setattr(self, stat, min(current + amount, self.MAX_STAT))

    def get_power_level(self) -> int:
        return self.ninjutsu + self.genjutsu + self.intelligence + self.resolve

    def is_weak(self) -> bool:
        return self.get_power_level() < 28

    def is_strong(self) -> bool:
        return self.get_power_level() > 35

    def reset_hp(self) -> None:
        self.hp = 100