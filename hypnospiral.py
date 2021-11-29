from random import randint
from math import sin, cos
class HypnoSpiral:
    """Отрисовывает перемещающиеся для создания эффекта окружности.

    АТРИБУТЫ:
    ---------
    __coord : list, int         -- координаты x и y центра общей окружности.
    __speed : list, int         -- скорость изменения по осям.
    __colors : list, tuple      -- список с цветом окружностей.
                                   Генерируется на основе случайных чисел.
    __radius : list, int        -- радиус окружностей.
                                   Генерируется приращением к базовой величине.

    МЕТОДЫ:
    -------
    __draw(scene)        -- формирует изображение на экране.
    __act()              -- изменяет координаты.

    ПРИМЕЧАНИЕ:
    -----------

    """
    def __init__(self, x, y,         # Координаты x, y
                 speed_x, speed_y,   # Изменение скорости по x, y
                 max_color_red,    # Диапазон цвета для красного канала: tuple
                 max_color_green,  # Диапазон цвета для зелёного канала: tuple
                 max_color_blue,   # Диапазон цвета для синего канала: tuple
                 count_circles,      # Количество кругов
                 min_radius,         # Начальный (базовый) радиус
                 max_radius):        # Максимальный радиус
        """Определение параметров."""
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__coord = []
        self.__speed = []
        self.__colors = []
        self.__count_circles = count_circles
        self.__radius = []
        self.__default_x = x
        self.__default_y = y
        # Элементы по индексу [0] отвечают за координату x
        # Элементы по индексу [1] отвечают за координату y
        for i in range(count_circles):
            # Координаты и "скорость"
            self.__coord.append([x, y])
            self.__speed.append([i / 25, i / 25])

            # Задаём цвет
            self.__colors.append(((100 + i * 4) % max(1, max_color_red),
                                  ((100 + i * 4) % max(1, max_color_green)),
                                  ((100 + i * 4) % max(1, max_color_blue))))

            # Радиус от меньшего к большему
            self.__radius.append(min_radius + i % (max_radius - min_radius))

    def act(self):
        """Изменяет координаты каждого круга."""
        for i in range(len(self.__coord)):
            # Изменяем x и y
            self.__coord[i][0] += sin(self.__speed[i][0]) * 2
            self.__coord[i][1] += cos(self.__speed[i][1]) * 2

            self.__speed[i][0] += self.__speed_x
            self.__speed[i][1] += self.__speed_y

            if self.__speed[i][0] > self.__count_circles / 15:
                self.__speed[i][0] = i / 25
                self.__coord[i][0] = self.__default_x

            if self.__speed[i][1] > self.__count_circles / 15:
                self.__speed[i][1] = i / 25
                self.__coord[i][1] = self.__default_y

    # Обязательно передаём pygame и сцену, на которой рисовать круги
    def draw(self, pygame, scene):
        """Формирует изображение."""
        for i in range(len(self.__coord)):
            pygame.draw.circle(scene,
                               self.__colors[i],
                               (self.__coord[i][0], self.__coord[i][1]),
                               self.__radius[i],
                               2)
