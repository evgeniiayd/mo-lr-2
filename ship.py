import os
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Класс для представления корабля игрока."""

    def __init__(self, ai_game):
        """
        Инициализирует корабль и задает его начальную позицию.

        Args:
            ai_game (AlienInvasion): Экземпляр класса AlienInvasion, который содержит параметры игры.
        """
        super().__init__()
        self.screen = ai_game.screen  # Экран, на котором будет отображаться корабль
        self.settings = ai_game.settings  # Настройки игры
        self.screen_rect = ai_game.screen.get_rect()  # Прямоугольник экрана

        # Загружает изображение корабля и получает прямоугольник
        resource_path = os.path.join('resources', 'ship2.png')  # Путь к изображению
        self.image = pygame.image.load(resource_path)  # Загрузка изображения
        self.rect = self.image.get_rect()  # Получение прямоугольника изображения

        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom  # Установка начальной позиции
        self.x = float(self.rect.x)  # Позиция по оси x в виде числа с плавающей точкой

        # Флаги перемещения
        self.moving_right = False  # Флаг перемещения вправо
        self.moving_left = False   # Флаг перемещения влево

    def update(self):
        """
        Обновляет позицию корабля с учетом флагов перемещения.
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed  # Увеличение позиции x при движении вправо
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed  # Уменьшение позиции x при движении влево

        self.rect.x = self.x  # Обновление прямоугольника по оси x

    def blitme(self):
        """
        Рисует корабль в текущей позиции.
        """
        self.screen.blit(self.image, self.rect)  # Отображение изображения корабля на экране

    def center_ship(self):
        """
        Центрирует корабль в нижней части экрана.
        """
        self.rect.midbottom = self.screen_rect.midbottom  # Установка позиции корабля
        self.x = float(self.rect.x)  # Обновление позиции x

