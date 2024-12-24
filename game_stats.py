class GameStats:
    """Класс для отслеживания статистики игры."""

    def __init__(self, ai_game):
        """
        Инициализирует статистику игры.

        Args:
            ai_game (object): Экземпляр основного игрового класса, содержащий настройки игры.
        """
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра активна или нет.
        self.game_active = False

    def reset_stats(self):
        """
        Сбрасывает статистику, которая может изменяться во время игры.
        """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1


