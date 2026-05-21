from engine.character import Character


class Display:

    @staticmethod
    def narrate(text: str, delay: float = 0.03) -> None:
        pass

    @staticmethod
    def dialogue(speaker: str, text: str) -> None:
        pass

    @staticmethod
    def show_stats(character: Character) -> None:
        pass

    @staticmethod
    def chapter_title(title: str) -> None:
        pass

    @staticmethod
    def choice(options: list[str]) -> int:
        pass

    @staticmethod
    def separator() -> None:
        """Горизонтальна лінія-розділювач між сценами."""
        pass

    @staticmethod
    def pause(message: str = "Натисни Enter щоб продовжити...") -> None:
        pass