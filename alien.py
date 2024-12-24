import os
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс для представления одного пришельца в флоте."""

    def __init__(self, ai_game):
        """
        Инициализирует пришельца и устанавливает его начальную позицию.

        Args:
            ai_game (object): Экземпляр основного игрового класса, содержащий настройки и экран.

        Returns:
            None
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Определение пути к ресурсу
        resource_path = os.path.join('resources', 'alien1.jpg')
        # Загрузка изображения
        self.image = pygame.image.load(resource_path)
        self.rect = self.image.get_rect()

        # Начинаем каждого нового пришельца в верхнем левом углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Храним точную позицию пришельца.
        self.x = float(self.rect.x)

    def check_edges(self):
        """
        Проверяет, достиг ли пришелец края экрана.

        Returns:
            bool: True, если пришелец достиг края экрана (правого или левого), иначе False.
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """
        Обновляет позицию пришельца, перемещая его в зависимости от скорости и направления флота.

        Args:
            None

        Returns:
            None
        """
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x



