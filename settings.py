class Settings():
    """Настройки игры."""

    def __init__(self):
        """
        Инициализирует статические настройки игры.
        """
        self.width = 1200  # Ширина экрана
        self.height = 720   # Высота экрана
        self.bg_color = (255, 203, 219)  # Цвет фона
        self.bullets_allowed = 3  # Максимальное количество снарядов

        # Настройки корабля
        self.ship_speed = 1.5  # Скорость корабля
        self.ship_limit = 3     # Ограничение на количество кораблей

        # Параметры снаряда
        self.bullet_speed = 1.5  # Скорость снаряда
        self.bullet_width = 3     # Ширина снаряда
        self.bullet_height = 15    # Высота снаряда
        self.bullet_color = (60, 60, 60)  # Цвет снаряда

        # Настройки пришельцев
        self.alien_speed = 0.5  # Скорость пришельца
        self.fleet_drop_speed = 5  # Скорость падения флота
        self.fleet_direction = 1  # Направление движения флота (1 - вправо, -1 - влево)

        # Темп ускорения игры
        self.speedup_scale = 1.1  # Коэффициент ускорения
        self.score_scale = 1.5     # Коэффициент увеличения очков
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        Инициализирует настройки, которые изменяются в процессе игры.
        """
        self.ship_speed_factor = 1.5  # Фактор скорости корабля
        self.bullet_speed_factor = 3    # Фактор скорости снаряда
        self.alien_speed_factor = 1      # Фактор скорости пришельца

        # fleet_direction равен 1, что означает движение вправо, -1 - влево.
        self.fleet_direction = 1
        self.alien_points = 50  # Очки за уничтожение пришельца

    def increase_speed(self):
        """
        Увеличивает настройки скорости и значения очков за пришельцев.
        """
        self.ship_speed_factor *= self.speedup_scale  # Увеличивает скорость корабля
        self.bullet_speed_factor *= self.speedup_scale  # Увеличивает скорость снаряда
        self.alien_speed_factor *= self.speedup_scale    # Увеличивает скорость пришельца

        self.alien_points = int(self.alien_points * self.score_scale)  # Увеличивает очки за пришельца
