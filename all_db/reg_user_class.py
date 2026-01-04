import sqlite3

class DbRegUsers():
    def __init__(self) -> None:
        with sqlite3.connect('D:/script/remaster_bot/all_db/reg_users.db') as db:
            self.db = db
            self.cur = db.cursor()

    def reg_user(self, user_id: int, name: str):
        self.cur.execute('SELECT count(id) FROM users WHERE id = ?', (user_id, ))
        if self.cur.fetchone()[0] == 0:
            self.cur.execute('INSERT INTO users VALUES(?, ?, ?)', (user_id, name, 'YES'))
        else:
            pass
        self.db.commit()