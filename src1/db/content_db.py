import os
import sqlite3
from typing import Callable

from __version__ import __version__, release_history
from model.content_frag import ContentFragType


class DBInfoKey:
    version = 'version'


class ContentDB(sqlite3.Connection):

    def __init__(self, file_path: str):
        file_exists = os.path.exists(file_path)

        super().__init__(file_path)
        self.isolation_level = None  # 开启自动提交
        self.execute('pragma journal_mode=wal;')

        if file_exists:
            self.transaction(self._update_data_structure)
        else:
            self.transaction(self._create_data_structure)

    def transaction(self, func: Callable[[], None]) -> None:
        """
        事务处理

        Args:
            func: 事务内要执行的函数

        """
        try:
            self.execute("BEGIN")
            func()
            self.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.rollback()
            raise e

    def _create_data_structure(self) -> None:
        # DDL
        ddl = '''
DROP TABLE IF EXISTS db_info;
CREATE TABLE db_info
(
    k TEXT PRIMARY KEY,
    v TEXT NOT NULL
);

DROP TABLE IF EXISTS batch;
CREATE TABLE batch
(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    version TEXT    NOT NULL,
    time    INTEGER NOT NULL,
    config  TEXT    NOT NULL
);

DROP TABLE IF EXISTS content_fragment_type;
CREATE TABLE content_fragment_type
(
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    label TEXT NOT NULL
);

DROP TABLE IF EXISTS post;
CREATE TABLE post
(
    id               INTEGER PRIMARY KEY,
    contents         TEXT               NOT NULL, 
    floor            INTEGER            NOT NULL, 

    agree            INTEGER DEFAULT 0  NOT NULL,
    disagree         INTEGER DEFAULT 0  NOT NULL,
    create_time      INTEGER            NOT NULL,
    is_thread_author BOOLEAN DEFAULT 0  NOT NULL, 

    sign             TEXT    DEFAULT '' NOT NULL, 
    reply_num        INTEGER DEFAULT 0  NOT NULL, 

    parent_id        INTEGER DEFAULT 0  NOT NULL, 
    reply_to_id      INTEGER DEFAULT 0  NOT NULL, 
    thread_id        INTEGER            NOT NULL,
    author_id        INTEGER            NOT NULL,

    batch            INTEGER            NOT NULL,
    update_batch     INTEGER            NOT NULL
);
CREATE INDEX 'idx_post(floor)' ON post (floor);
CREATE INDEX 'idx_post(author_id)' ON post (author_id);
CREATE INDEX 'idx_post(agree)' ON post (agree);
CREATE INDEX 'idx_post(create_time)' ON post (create_time);
CREATE INDEX 'idx_post(is_thread_author)' ON post (is_thread_author);
CREATE INDEX 'idx_post(parent_id)' ON post (parent_id);
CREATE INDEX 'idx_post(batch)' ON post (batch);
CREATE INDEX 'idx_post(update_batch)' ON post (update_batch);

DROP TABLE IF EXISTS thread;
CREATE TABLE thread
(
    id           INTEGER PRIMARY KEY,
    title        TEXT               NOT NULL,
    contents     TEXT               NOT NULL, 
    type         INTEGER DEFAULT 0  NOT NULL,
    is_share     BOOLEAN DEFAULT 0  NOT NULL,
    is_help      BOOLEAN DEFAULT 0  NOT NULL,
    vote_info    TEXT    DEFAULT '' NOT NULL, 
    share_origin INTEGER DEFAULT 0  NOT NULL,
    view_num     INTEGER DEFAULT 0  NOT NULL,
    reply_num    INTEGER DEFAULT 0  NOT NULL,
    share_num    INTEGER DEFAULT 0  NOT NULL,
    agree        INTEGER DEFAULT 0  NOT NULL,
    disagree     INTEGER DEFAULT 0  NOT NULL,
    create_time  INTEGER            NOT NULL,

    forum_id     INTEGER            NOT NULL,
    post_id      INTEGER            NOT NULL, 
    author_id    INTEGER            NOT NULL,

    status       INTEGER DEFAULT 0  NOT NULL  
);

DROP TABLE IF EXISTS forum;
CREATE TABLE forum
(
    id          INTEGER PRIMARY KEY,
    name        TEXT               NOT NULL,
    category    TEXT    DEFAULT '' NOT NULL,
    subcategory TEXT    DEFAULT '' NOT NULL,
    member_num  INTEGER DEFAULT 0  NOT NULL,
    post_num    INTEGER DEFAULT 0  NOT NULL,
    thread_num  INTEGER DEFAULT 0  NOT NULL,
    slogan      TEXT    DEFAULT '' NOT NULL,
    avatar      TEXT    DEFAULT '' NOT NULL
);

DROP TABLE IF EXISTS 'user';
CREATE TABLE user
(
    id         INTEGER DEFAULT NULL NULL,     
    portrait   TEXT    DEFAULT NULL NULL,     
    tieba_uid  INTEGER DEFAULT NULL NULL,     
    username   TEXT    DEFAULT ''   NOT NULL, 
    nickname   TEXT    DEFAULT ''   NOT NULL, 

    glevel     INTEGER DEFAULT 0    NOT NULL, 
    gender     INTEGER DEFAULT 0    NOT NULL, 
    ip         TEXT    DEFAULT ''   NOT NULL,
    is_vip     BOOLEAN DEFAULT 0    NOT NULL, 
    is_god     BOOLEAN DEFAULT 0    NOT NULL, 
    age        FLOAT   DEFAULT 0    NOT NULL, 
    sign       TEXT    DEFAULT ''   NOT NULL, 
    post_num   INTEGER DEFAULT 0    NOT NULL, 
    agree_num  INTEGER DEFAULT 0    NOT NULL, 
    fan_num    INTEGER DEFAULT 0    NOT NULL, 
    follow_num INTEGER DEFAULT 0    NOT NULL, 
    forum_num  INTEGER DEFAULT 0    NOT NULL, 

    level      INTEGER DEFAULT 0    NOT NULL, 
    is_bawu    BOOLEAN DEFAULT 0    NOT NULL, 

    avatar     TEXT    DEFAULT ''   NOT NULL, 
    status     INTEGER DEFAULT 0    NOT NULL, 
    batch      INTEGER              NOT NULL  
);
CREATE UNIQUE INDEX 'uk_user(id)' ON 'user' (id);
CREATE UNIQUE INDEX 'uk_user(portrait)' ON 'user' (portrait);
CREATE UNIQUE INDEX 'uk_user(tieba_uid)' ON 'user' (tieba_uid);

DROP TABLE IF EXISTS tieba_origin_src;
CREATE TABLE tieba_origin_src
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    filename   TEXT NOT NULL,
    origin_src TEXT NOT NULL
);
CREATE UNIQUE INDEX 'uk_tieba_origin_src(filename)' ON tieba_origin_src (filename);
'''

        self.executescript(ddl)

        self.executemany('INSERT INTO db_info(k, v) VALUES (?, ?);', [
            (DBInfoKey.version, __version__),
        ])

        self.executemany(
            'INSERT INTO content_fragment_type(id, label) VALUES (?, ?);',
            list(map(lambda x: (x.value, x.label), ContentFragType))
        )

    def _update_data_structure(self):
        current_version = self._get_db_info_item(DBInfoKey.version)

        if current_version == __version__:
            return

        # TODO LOG 开始更新数据库。

        anchor = release_history.index(current_version)
        # 模拟 switch...case... 连续升级
        if release_history.index('2.0.0') > anchor:
            self.executescript('''''')

        self._update_db_info_item(DBInfoKey.version, __version__)

    def _update_db_info_item(self, k: str, v: str):
        sql_key_exists = 'SELECT 1 FROM db_info WHERE k = ?'
        sql_update = 'UPDATE db_info SET v = ? WHERE k = ?'
        sql_insert = 'INSERT INTO db_info(k, v) VALUES (?, ?)'

        if self.execute(sql_key_exists, (k,)).fetchone():
            self.execute(sql_update, (v, k))
        else:
            self.execute(sql_insert, (k, v))

    def _get_db_info_item(self, k: str) -> str:
        sql = 'SELECT v FROM db_info WHERE k = ?'
        return self.execute(sql, (k,)).fetchone()[0]
