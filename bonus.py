import pygame
from pygame.sprite import Sprite


class Bonus(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/potion.png')
        self.rect = self.image.get_rect()

        self.rect.midtop = self.screen_rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y += 1
        self.rect.y = self.y

    def blitme(self):
        """Рисует зелье в текущей позиции"""
        self.screen.blit(self.image, self.rect)