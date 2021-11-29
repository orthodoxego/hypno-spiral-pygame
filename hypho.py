# Подключаем pygame
import pygame
from hypnospiral import HypnoSpiral
from random import randint

class Game:
    """Класс-шаблон для игр на базе pygame.

    Для старта необходимо вызвать метод run().

    АТРИБУТЫ:
    ---------
    BLACK, WHITE, RED,
    GREEN, BLUE : tuple         -- цвета в RGB.
    __WIDTH, __HEIGHT : int     -- ширина и высота окна.
                                   Для них определены геттеры @property.
    __FPS : int                 -- количество кадров в секунду.

    МЕТОДЫ:
    -------
    __init__(ШИРИНА: int,
             ВЫСОТА: int,
             ЗАГОЛОВОК: str,
             КАДРЫ_В_СЕКУНДУ: int) -- конструктор класса.
    __draw()                       -- формирует изображение.
    __act()                        -- сюда вставить необходимые расчёты.
    run()                          -- запуск pygame.

    ПРИМЕЧАНИЕ:
    -----------
    Образец для запуска кода:
    game = Game(1024, 768, "Шаблон pygame", 60)
    game.run()
    """
    # Задаём цвета
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    def __init__(self, width, height, caption, fps):
        """Конструктор, настройка основных параметров."""
        # Инициализация pygame и настройки окна
        pygame.init()

        # Настройка ширины и высоты окна
        self.__WIDTH = width
        self.__HEIGHT = height

        if width * height == 0:
            self.__WIDTH = pygame.display.Info().current_w
            self.__HEIGHT = pygame.display.Info().current_h

        self.__size = [self.__WIDTH, self.__HEIGHT]

        # Установка заголовка окна
        pygame.display.set_caption(caption)

        # Инициализация сцены и установка размера
        if width * height != 0:
            self.scene = pygame.display.set_mode(self.__size)
        else:
            self.scene = pygame.display.set_mode(flags=pygame.FULLSCREEN)

        # Для работы с задержкой и организации FPS
        self.clock = pygame.time.Clock()
        self.__FPS = fps

        # Маркер "идёт ли игра"
        self.playGame = True

        # Создаём бублики
        self.hypno = []
        self.hypno.append(HypnoSpiral(self.__WIDTH // 2, self.__HEIGHT // 2,
                                     0.009, 0.009,
                                     255, 0, 50,
                                     256,
                                     32, 64))

        self.hypno.append(HypnoSpiral(self.__WIDTH // 2, self.__HEIGHT // 2,
                                     0.01, 0.01,
                                     0, 155, 255,
                                     256,
                                     16, 32))

        self.hypno.append(HypnoSpiral(self.__WIDTH // 2, self.__HEIGHT // 2,
                                     0.015, 0.015,
                                     50, 255, 0,
                                     128,
                                     8, 16))


    @property
    def WIDTH(self):
        return self.__WIDTH

    @property
    def HEIGHT(self):
        return self.__HEIGHT

    def __draw(self):
        """Формирует изображение.
        Вызывать метод следует между очисткой и обновлением экрана."""
        for h in self.hypno:
            h.draw(pygame, self.scene)

    def __act(self):
        """Метод для расчётов. Вызывать после обновления экрана."""
        for h in self.hypno:
            h.act()

    def run(self):
        """Главный цикл игры."""
        while (self.playGame):
            # Проверяем нажатые клавиши
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.playGame = False
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_ESCAPE):
                        self.playGame = False
                    elif (event.key == pygame.K_LEFT):
                        print("ВЛЕВО")
                    elif (event.key == pygame.K_RIGHT):
                        print("ВПРАВО")
                    elif (event.key == pygame.K_UP):
                        print("ВВЕРХ")
                    elif (event.key == pygame.K_DOWN):
                        print("ВНИЗ")

            # Очищаем сцену
            self.scene.fill(self.BLACK)

            # Формируем изображение
            self.__draw()

            # Отрисовываем изображения
            pygame.display.flip()

            # Расчёты
            self.__act()

            # Задержка для синхронизации FPS
            self.clock.tick(self.__FPS)

        # Выход
        pygame.quit()

if __name__ == "__main__":
    # Для запуска в полноэкранном режиме
    game = Game(0, 0, "Гипноспираль", 60)
    # game = Game(1600, 1050, "Гипноспираль", 60)
    game.run()
