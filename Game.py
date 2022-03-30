from random import choice
from PyQt5.QtCore import QPropertyAnimation, QAbstractAnimation, QEasingCurve, QRect
from PyQt5.QtWidgets import QInputDialog
from Table import Table
from Tiles import *
from Models import *


class Game:
    def __init__(self, window, widget, score, best, modal):
        self.SPLITTER_SIZE = [770, 140]
        self.WIDGET_COORD = [140, 170]
        self.WIDGET_PADDING = 40
        self.TILES_MARGIN = 10
        self.NEW_USER = 'Создать нового пользователя'
        self._sides_count = 4
        self._widget_size_side = 0
        self._score_property = 0
        self._best_score = 0
        self.player: Player = 0
        self.setting: Setting = 0
        self.modal_animation = 0
        self.label__score = score
        self.label__best = best
        self.modal = modal
        self.widget = widget
        self.window = window
        self.settings = {}
        self.animations = []
        self.tiles = []
        self.old_tiles = ''
        self.can_move = False
        self.is_win = False
        TileFactory.create(window, widget)

    def prepare_objects(self):
        player_id, btn_ok = self.choose_player()
        if not btn_ok:
            return False
        self.player = Player.get_model(f'player_id == {player_id}')
        self.setting = Setting.get_model(f'player_id == {self.player.player_id}')
        if self.setting is None:
            self.setting = Setting(1, 4, 0, self.player.player_id)
        return True

    def start(self):
        self.sides_count = self.setting.sides_count
        # Восстанавливаем состояние, если ход больше чем 1
        if self.setting.step > 1:
            self.restore_snapshot(self.setting.step, self.player.player_id)
        else:
            self.delete_snapshots(self.setting.step, self.player.player_id)
            self.tiles = TileFactory.create_tiles(self.sides_count, self.sides_count)
            for i in range(2):
                self.add_tile(*self.have_free_space())
        self.old_tiles = self.encode_tiles()
        self.best_score = self.get_best_score(self.player.player_id)
        self.widget_side_size = self.sides_count
        self.settings = {
            'j_range': [
                [1, self.sides_count, 1],
                [self.sides_count - 2, -1, -1],
                [1, self.sides_count, 1],
                [self.sides_count - 2, -1, -1]
            ],
            'k_range': [
                [-1, -1, -1],
                [1, self.sides_count, 1],
                [-1, -1, -1],
                [1, self.sides_count, 1]
            ],
            'next_button': [1, -1, 1, -1],
            'row': ['i', 'i', 'k', 'k'],
            'col': ['k', 'k', 'i', 'i'],
            'reverse': [False, False, True, True]
        }
        self.can_move = True
        self.modal.hide()
        self.update_field()

    def restart(self):
        sides_count, ok = QInputDialog.getInt(
            self.window,
            'Количество плиток',
            'Плиток в строке',
            self.sides_count,
            4, 7, 1
        )
        if ok:
            last_player_id = self.player.player_id
            last_score = self.score_property
            if not self.prepare_objects():
                return
            Score(last_score, last_player_id)
            self.score_property = 0
            self.setting.step = 1
            self.sides_count = sides_count
            self.delete_tiles()
            self.modal.hide()
            self.start()

    def undo(self):
        if self.setting.step > 2:
            self.modal.hide()
            self.setting.step -= 1
            self.restore_snapshot(self.setting.step, self.player.player_id)

    def change_user(self):
        if not self.prepare_objects():
            return
        self.score_property = self.setting.score
        self.delete_tiles()
        self.modal.hide()
        self.start()

    def show_table(self):
        data = {
            'headers': ['Игрок', 'Счет'],
            'players': self.get_best_players()
        }
        self.table = Table(self.window, data)
        self.table.exec()

    def shift(self, index):
        for i in range(self.sides_count):
            for j in range(*self.settings['j_range'][index]):
                for k in range(j + self.settings['k_range'][index][0], *self.settings['k_range'][index][1:]):
                    row = eval(bytes(self.settings['row'][index], encoding='utf8'))
                    col = eval(bytes(self.settings['col'][index], encoding='utf8'))
                    next_number = self.settings['next_button'][index]
                    reverse = self.settings['reverse'][index]
                    button = self.tiles[row][col]
                    button_number = (row, col)
                    if reverse:
                        next_button = self.tiles[row + next_number][col]
                        next_button_number = (row + next_number, col)
                    else:
                        next_button = self.tiles[row][col + next_number]
                        next_button_number = (row, col + next_number)
                    first_is_game_tile = isinstance(button, GameTile)
                    second_is_game_tile = isinstance(next_button, GameTile)
                    if not first_is_game_tile and second_is_game_tile:
                        self.move_tile(next_button_number, button_number)
                        if reverse:
                            self.tiles[row][col], self.tiles[row + next_number][col] = \
                                self.tiles[row + next_number][col], self.tiles[row][col]
                        else:
                            self.tiles[row][col], self.tiles[row][col + next_number] = \
                                self.tiles[row][col + next_number], self.tiles[row][col]
                    elif first_is_game_tile and second_is_game_tile:
                        if button.number == next_button.number:
                            new_button = next_button + button
                            if not self.is_win and new_button.number >= 2048:
                                self.is_win = True
                            next_button.deleteLater()
                            button.deleteLater()
                            self.tiles[row][col] = TileFactory.create_tile()
                            if reverse:
                                self.tiles[row + next_number][col] = new_button
                            else:
                                self.tiles[row][col + next_number] = new_button
                            self.set_tile_coord(new_button, *next_button_number)
                            self.move_tile(next_button_number, button_number)
                            self.score_property += new_button.number
                            if reverse:
                                self.tiles[row][col], self.tiles[row + next_number][col] = \
                                    self.tiles[row + next_number][col], self.tiles[row][col]
                            else:
                                self.tiles[row][col], self.tiles[row][col + next_number] = \
                                    self.tiles[row][col + next_number], self.tiles[row][col]

    def can_shifted(self, index):
        for i in range(self.sides_count):
            for j in range(*self.settings['j_range'][index]):
                for k in range(j + self.settings['k_range'][index][0], *self.settings['k_range'][index][1:]):
                    row = eval(bytes(self.settings['row'][index], encoding='utf8'))
                    col = eval(bytes(self.settings['col'][index], encoding='utf8'))
                    next_number = self.settings['next_button'][index]
                    reverse = self.settings['reverse'][index]
                    button = self.tiles[row][col]
                    if reverse:
                        next_button = self.tiles[row + next_number][col]
                    else:
                        next_button = self.tiles[row][col + next_number]
                    first_is_game_tile = isinstance(button, GameTile)
                    second_is_game_tile = isinstance(next_button, GameTile)
                    if not first_is_game_tile and second_is_game_tile:
                        return True
                    elif first_is_game_tile and second_is_game_tile:
                        if button.number == next_button.number:
                            return True
        return False

    def move(self, shift):
        self.can_move = self.check_game()
        if self.can_move:
            self.setting.step += 1
            self.old_tiles = self.encode_tiles()
            self.shift(shift)
            if self.field_changed():
                coord = self.have_free_space()
                if coord:
                    self.add_tile(*coord)
            if self.setting.step > 1:
                Snapshot(
                    self.setting.step,
                    self.encode_tiles(),
                    self.is_win,
                    self.score_property,
                    self.player.player_id
                )
            # Из-за этого плавность пропадает, возможны несостыковки (пока что все нормально)
            # self.update_field()
        else:
            if self.modal.isHidden():
                self.show_end_modal()

    def field_changed(self):
        return self.old_tiles != self.encode_tiles()

    def have_free_space(self):
        coord = []
        for i, row in enumerate(self.tiles):
            for j, tile in enumerate(row):
                if not isinstance(tile, GameTile):
                    coord.append([i, j])
        return choice(coord) if coord else []

    def check_game(self):
        return any([self.can_shifted(i) for i in range(4)])

    def show_end_modal(self):
        size = self.widget.height()
        geometry = QRect(self.widget.x(), self.widget.y() + size, size, size)
        text = 'Вы выиграли' if self.is_win else 'Вы проиграли'
        self.modal.setText(text)
        self.modal.show()
        self.modal_animation = QPropertyAnimation(self.modal, b'geometry')
        self.modal_animation.setDuration(500)
        self.modal_animation.setEasingCurve(QEasingCurve.Linear)
        self.modal_animation.setStartValue(geometry)
        self.modal_animation.setEndValue(self.widget.geometry())
        self.modal_animation.start(QAbstractAnimation.DeleteWhenStopped)

    def choose_player(self):
        players_names = [self.NEW_USER]
        players_names += [player.name for player in Player.get_models()]
        player_id, btn_ok = self.get_player_id(players_names)
        if not btn_ok:
            return player_id, btn_ok
        while not player_id:
            name, btn_ok = QInputDialog.getText(self.window, "Игрок", "Введите никнейм")
            if not name or not btn_ok:
                player_id = self.get_player_id(players_names)
            else:
                player_id = len(players_names)
                Player(player_id, name)
        return player_id, btn_ok

    def get_player_id(self, players_names):
        name, btn_ok = QInputDialog.getItem(
            self.window,
            "Игрок",
            "Выберите игрока",
            players_names,
            0,
            False
        )
        player_id = 0
        if btn_ok:
            player_id = players_names.index(name)
        return player_id, btn_ok

    def add_tile(self, i, j):
        self.tiles[i][j].deleteLater()
        self.tiles[i][j] = TileFactory.create_game_tile()
        self.set_tile_coord(self.tiles[i][j], i, j)
        return self.tiles[i][j]

    def move_tile(self, start, end):
        i, j = start
        tile = self.tiles[i][j]
        tile_side_size = Tile.tile_side_size()
        anim = QPropertyAnimation(tile, b'geometry')
        anim.setParent(tile)
        anim.setDuration(300)
        anim.setEasingCurve(QEasingCurve.Linear)
        anim.setEndValue(QRect(*self.get_tile_coord(*end), tile_side_size, tile_side_size))
        anim.start(QAbstractAnimation.DeleteWhenStopped)
        if len(self.animations) > 100:
            self.animations.clear()
        # Добавляем объект анимации в список, дабы его не удалил сборщик мусора
        self.animations.append(anim)

    def get_tile_coord(self, i, j):
        distance = Tile.tile_side_size() + self.tiles_margin
        return (self.widget_padding + j * distance,
                self.widget_padding + i * distance)

    def set_tile_coord(self, tile, i, j):
        tile.move(*self.get_tile_coord(i, j))

    def update_field(self):
        for i, row in enumerate(self.tiles):
            for j, tile in enumerate(row):
                tile.move(*self.get_tile_coord(i, j))

    def encode_tiles(self):
        return '#'.join(['-'.join(map(str, row)) for row in self.tiles])

    def decode_tiles(self, string):
        return [[TileFactory.create_game_tile(int(tile)) if int(tile) else TileFactory.create_tile()
                 for tile in row.split('-')]
                for row in string.split('#')]

    def delete_tiles(self):
        for i in self.tiles:
            for j in i:
                j.deleteLater()

    def get_best_score(self, player_id):
        scores = [score.score for score in Score.filter_models(f'model.player_id == {player_id}')]
        return max(scores) if scores else 0

    def get_best_players(self):
        players = []
        for player in Player.get_models():
            try:
                players.append([
                    player.name,
                    str(max(map(lambda x: x.score, Score.filter_models(f'model.player_id == {player.player_id}'))))
                ])
            except ValueError:
                pass
        players.sort(key=lambda x: int(x[1]), reverse=True)
        return players

    def get_players(self):
        Player.load_models()

    def get_settings(self):
        Setting.load_models()

    def get_snapshots(self):
        Snapshot.load_models()

    def get_scores(self):
        Score.load_models()

    def save_players(self):
        Player.save_models()

    def save_settings(self):
        Setting.save_models()

    def save_snapshots(self):
        Snapshot.save_models()

    def save_scores(self):
        Score.save_models()

    def restore_snapshot(self, step, player_id):
        snapshot = Snapshot.get_model(f'step == {step}', f'player_id == {player_id}')
        self.delete_snapshots(step, player_id)
        self.delete_tiles()
        self.tiles = self.decode_tiles(snapshot.encoded_tiles)
        self.is_win = snapshot.is_win
        self.score_property = snapshot.score
        self.update_field()

    def delete_snapshots(self, step, player_id):
        Snapshot.delete_models(f'step > {step}', f'player_id == {player_id}')

    @property
    def widget_padding(self):
        return self.WIDGET_PADDING

    @property
    def tiles_margin(self):
        return self.TILES_MARGIN

    @property
    def widget_side_size(self):
        return self._widget_size_side

    @widget_side_size.setter
    def widget_side_size(self, value):
        size = Tile.tile_side_size()
        widget_size = size * value + self.tiles_margin * (value - 1) + self.widget_padding * 2
        widget_x = self.SPLITTER_SIZE[0] // 2 - widget_size // 2
        widget_y = self.widget.y()
        self.window.setFixedHeight(widget_y + widget_size + 50)
        self.window.setFixedWidth(widget_x * 2 + widget_size)
        self._widget_size_side = widget_size
        self.widget.setGeometry(widget_x, widget_y, widget_size, widget_size)

    @property
    def sides_count(self):
        return self._sides_count

    @sides_count.setter
    def sides_count(self, value):
        self._sides_count = value
        self.setting.sides_count = value

    @property
    def score_property(self):
        return self._score_property

    @score_property.setter
    def score_property(self, value):
        self._score_property = value
        self.setting.score = value
        self.label__score.setText(str(self._score_property))
        if self._score_property > int(self.label__best.text()):
            self.label__best.setText(str(self._score_property))

    @property
    def best_score(self):
        return self._best_score

    @best_score.setter
    def best_score(self, value):
        self._best_score = value
        self.label__best.setText(str(value) if value > self.score_property else str(self.score_property))
