import os
import pygame
from pygame.sprite import Sprite


class Bonus(Sprite):
    """Класс для представления бонуса в игре."""

    def __init__(self, ai_game):
        """
        Инициализирует бонус и устанавливает его начальную позицию.

        Args:
            ai_game (object): Экземпляр основного игрового класса, содержащий настройки и экран.

        """
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Определение пути к ресурсу
        resource_path = os.path.join('resources', 'potion.png')
        # Загрузка изображения
        self.image = pygame.image.load(resource_path)
        self.rect = self.image.get_rect()

        # Устанавливаем начальную позицию бонуса в центре верхней части экрана
        self.rect.midtop = self.screen_rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """
        Обновляет позицию бонуса, перемещая его вниз по экрану.
        """
        self.y += 1
        self.rect.y = self.y

    def blitme(self):
        """
        Рисует бонус в текущей позиции на экране.
        """
        self.screen.blit(self.image, self.rect)

