import pygame
from pygame.sprite import Sprite


import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления пулями, выстреливаемыми из корабля."""

    def __init__(self, ai_game):
        """
        Создает объект пули в текущей позиции корабля.

        Args:
            ai_game (object): Экземпляр основного игрового класса, содержащий настройки и экран.
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Создаем прямоугольник пули в позиции (0, 0), затем устанавливаем правильную позицию.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Храним десятичное значение для позиции пули.
        self.y = float(self.rect.y)

    def update(self):
        """
        Перемещает пулю вверх по экрану.
        """
        # Обновляем десятичную позицию пули.
        self.y -= self.settings.bullet_speed
        # Обновляем позицию прямоугольника.
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Рисует пулю на экране.
        """
        pygame.draw.rect(self.screen, self.color, self.rect)

