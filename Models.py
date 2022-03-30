from Database import Database


# Interface
class Model:
    TABLE = 'models'

    def to_list(self):
        pass

    @classmethod
    def load_models(cls):
        pass

    @classmethod
    def get_models(cls):
        pass

    @classmethod
    def save_models(cls):
        Database.save_models(cls.TABLE, cls.get_models())

    @classmethod
    def filter_models(cls, condition):
        return filter(lambda model: eval(condition), cls.get_models())

    @classmethod
    def get_model(cls, *args):
        for model in cls.get_models():
            flag = True
            for arg in args:
                if not eval(f'model.{arg}'):
                    flag = False
            if flag:
                return model

    @classmethod
    def delete_models(cls, *args):
        for model in cls.get_models():
            flag = True
            for arg in args:
                if not eval(f'model.{arg}'):
                    flag = False
            if flag:
                cls.remove_model(model)

    @classmethod
    def remove_model(cls, model):
        pass


class Player(Model):
    TABLE = 'players'
    players = []

    def __init__(self, player_id, name):
        self.player_id = player_id
        self.name = str(name)
        self.players.append(self)

    def to_list(self):
        return [
            self.player_id,
            self.name
        ]

    @classmethod
    def load_models(cls):
        cls.players.clear()
        for model in Database.get_models(cls.TABLE):
            Player(*model)

    @classmethod
    def get_models(cls):
        return cls.players.copy()

    @classmethod
    def remove_model(cls, model):
        cls.players.remove(model)


class Score(Model):
    TABLE = 'scores'
    scores = []

    def __init__(self, score, player_id):
        self.score = score
        self.player_id = player_id
        self.scores.append(self)

    def to_list(self):
        return [
            self.score,
            self.player_id
        ]

    @classmethod
    def load_models(cls):
        cls.scores.clear()
        for model in Database.get_models(cls.TABLE):
            Score(*model)

    @classmethod
    def get_models(cls):
        return cls.scores.copy()

    @classmethod
    def remove_model(cls, model):
        cls.scores.remove(model)


class Snapshot(Model):
    TABLE = 'snapshots'
    snapshots = []

    def __init__(self, step, encoded_tiles, is_win, score, player_id):
        self.step = step
        self.encoded_tiles = encoded_tiles
        self.is_win = is_win
        self.score = score
        self.player_id = player_id
        self.snapshots.append(self)

    def to_list(self):
        return [
            self.step,
            self.encoded_tiles,
            self.is_win,
            self.score,
            self.player_id
        ]

    @classmethod
    def load_models(cls):
        cls.snapshots.clear()
        for model in Database.get_models(cls.TABLE):
            Snapshot(*model)

    @classmethod
    def get_models(cls):
        return cls.snapshots.copy()

    @classmethod
    def remove_model(cls, model):
        cls.snapshots.remove(model)


class Setting(Model):
    TABLE = 'settings'
    settings = []

    def __init__(self, step, sides_count, score, player_id):
        self.step = step
        self.sides_count = sides_count
        self.score = score
        self.player_id = player_id
        self.settings.append(self)

    def to_list(self):
        return [
            self.step,
            self.sides_count,
            self.score,
            self.player_id
        ]

    @classmethod
    def load_models(cls):
        cls.settings.clear()
        for model in Database.get_models(cls.TABLE):
            Setting(*model)

    @classmethod
    def get_models(cls):
        return cls.settings.copy()

    @classmethod
    def remove_model(cls, model):
        cls.settings.remove(model)
