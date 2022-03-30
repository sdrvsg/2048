from random import randint
from PyQt5.QtWidgets import QPushButton, QWidget, QMainWindow


class TileFactory:
    window: QMainWindow = 0
    widget: QWidget = 0

    @classmethod
    def create(cls, window, widget):
        cls.window = window
        cls.widget = widget

    @classmethod
    def create_tile(cls):
        tile = Tile(cls.widget)
        tile.installEventFilter(cls.window)
        return tile

    @classmethod
    def create_tiles(cls, rows, cols):
        return [[cls.create_tile() for _ in range(cols)] for _ in range(rows)]

    @classmethod
    def create_game_tile(cls, number=0):
        if not number:
            number = 4 if randint(1, 100) <= 10 else 2
        tile = GameTile(cls.widget, number)
        tile.installEventFilter(cls.window)
        return tile

    @classmethod
    def create_game_tiles(cls, rows, cols, number=0):
        return [[cls.create_game_tile(number) for _ in range(cols)] for _ in range(rows)]


class Tile(QPushButton):
    TILE_SIDE_SIZE = 70

    def __init__(self, widget):
        super().__init__(widget)
        self.widget = widget
        self.setFixedSize(self.tile_side_size(), self.tile_side_size())
        self.hide()

    def __str__(self):
        return '0'

    @classmethod
    def tile_side_size(cls):
        return cls.TILE_SIDE_SIZE


class GameTile(Tile):
    # Цвета для каждой цифры
    colors = {1: [80, 40, 25]}

    def __init__(self, widget, number):
        super().__init__(widget)
        self.number = number
        self.setText(str(number))
        if number not in self.colors.keys():
            self.colors[number] = self.generate_color(self.colors[list(self.colors.keys())[-1]])
        color = ', '.join(map(str, self.colors[number]))
        self.setStyleSheet(f'background-color: rgb({color});\n'
                           f'color: #F5F5F5;\n'
                           f'font-size: 24px;\n'
                           f'font-weight: bold;')
        self.show()

    def __add__(self, other):
        return TileFactory.create_game_tile(self.number + other.number)

    def __str__(self):
        return str(self.number)

    @staticmethod
    def generate_color(mix):
        # Генерируем цвет на основе предыдущего для большей сочетаемости
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        r = (r + mix[0]) // 2
        g = (g + mix[1]) // 2
        b = (b + mix[2]) // 2
        return [r, g, b]
