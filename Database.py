from sqlite3 import Connection, connect


class Database:
    DATABASE_NAME = 'Database.db'
    connection: Connection = 0

    @classmethod
    def connect(cls):
        cls.connection = connect(cls.DATABASE_NAME)

    @classmethod
    def get_models(cls, model):
        method = f'get_{model}_request'
        if hasattr(cls, method):
            request = getattr(cls, method)()
            cursor = cls.connection.cursor()
            result = cursor.execute(request).fetchall()
            if result is not None:
                for item in result:
                    yield item

    @classmethod
    def get_players_request(cls):
        return 'SELECT id, name FROM players'

    @classmethod
    def get_settings_request(cls):
        return 'SELECT step, sides_count, score, player_id FROM settings'

    @classmethod
    def get_snapshots_request(cls):
        return 'SELECT step, encoded_tiles, is_win, score, player_id FROM snapshots'

    @classmethod
    def get_scores_request(cls):
        return 'SELECT score, player_id FROM scores'

    @classmethod
    def save_models(cls, model, items):
        cursor = cls.connection.cursor()
        method = f'save_{model}_request'
        if hasattr(cls, method):
            request = getattr(cls, method)()
            cursor.execute(f'DELETE FROM {model}')
            cursor.executemany(request, map(lambda s: s.to_list(), items))
            cls.connection.commit()

    @classmethod
    def save_players_request(cls):
        return 'INSERT INTO players (id, name) VALUES (?, ?)'

    @classmethod
    def save_settings_request(cls):
        return 'INSERT INTO settings (step, sides_count, score, player_id) VALUES (?, ?, ?, ?)'

    @classmethod
    def save_snapshots_request(cls):
        return 'INSERT INTO snapshots (step, encoded_tiles, is_win, score, player_id) VALUES (?, ?, ?, ?, ?)'

    @classmethod
    def save_scores_request(cls):
        return 'INSERT INTO scores (score, player_id) VALUES (?, ?)'

    @classmethod
    def close(cls):
        if cls.connection:
            cls.connection.close()
