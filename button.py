import pygame.font
import pygame


class Button:
    """Класс для создания кнопки в игре."""

    def __init__(self, ai_game, msg):
        """
        Инициализирует атрибуты кнопки.

        Args:
            ai_game (object): Экземпляр основного игрового класса, содержащий экран.
            msg (str): Сообщение, которое будет отображаться на кнопке.
        """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Устанавливаем размеры и свойства кнопки.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Создаем объект rect кнопки и центрируем его.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Подготовка сообщения кнопки, которая требуется только один раз.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """
        Превращает сообщение в отрисованное изображение и центрирует текст на кнопке.

        Args:
            msg (str): Сообщение, которое будет отображаться на кнопке.
        """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """
        Рисует пустую кнопку, затем рисует сообщение на ней.
        """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

