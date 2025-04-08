-- (v1.3.1) 新增
DROP TABLE IF EXISTS batch;
CREATE TABLE batch
(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    version TEXT    NOT NULL,
    config  TEXT    NOT NULL,
    time    INTEGER NOT NULL
);



DROP TABLE IF EXISTS content_fragment_type;
CREATE TABLE content_fragment_type
(
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL
);


DROP TABLE IF EXISTS aa;
CREATE TABLE aa
(
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL
);



DROP TABLE IF EXISTS post;
CREATE TABLE post
(
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    contents         TEXT               NOT NULL, -- json [{ type: 1, }]
    floor            INTEGER            NOT NULL, -- 楼和楼中楼一样
    user_id          INTEGER            NOT NULL,
    agree            INTEGER DEFAULT 0  NOT NULL,
    disagree         INTEGER DEFAULT 0  NOT NULL,
    create_time      INTEGER            NOT NULL, -- 创建时间，要依赖爬取的时间
    is_thread_author BOOLEAN DEFAULT 0  NOT NULL, -- 冗余字段， 区分楼主和普通用户
    sign             TEXT    DEFAULT '' NOT NULL, -- 小尾巴，post独有,
    reply_num        INTEGER DEFAULT 0  NOT NULL, -- 楼独有，冗余字段，不需要join。
    parent_id        INTEGER DEFAULT 0  NOT NULL, -- 楼中楼独有, 区分普通楼和楼中的唯一标识 "where parent_id == 0"
    reply_to_id      INTEGER DEFAULT 0  NOT NULL, -- 楼中楼独有，不是所有的楼中楼都有reply_to_id。回复给谁,是uid不是 pid。

    batch_id         INTEGER DEFAULT 0  NOT NULL, -- (v1.3.1 - 新增) 关联 scrape_batch.id
    update_batch_id  INTEGER DEFAULT 0  NOT NULL
);
CREATE INDEX 'idx_post(floor)' ON post(floor);
CREATE INDEX 'idx_post(user_id)' ON post(user_id);
CREATE INDEX 'idx_post(agree)' ON post(agree); -- 根据点赞数排序
CREATE INDEX 'idx_post(create_time)' ON post(create_time); -- 根据创建时间排序
CREATE INDEX 'idx_post(is_thread_author)' ON post(is_thread_author); -- 根据楼主和普通用户区分
CREATE INDEX 'idx_post(parent_id)' ON post(parent_id);
CREATE INDEX 'idx_post(batch_id)' ON post(batch_id);-- (v1.3.1)新增


DROP TABLE IF EXISTS origin_src;
CREATE TABLE origin_src
(
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    filename          TEXT    NOT NULL,
    content_frag_type INTEGER NOT NULL,
    origin_src        TEXT    NOT NULL
);
CREATE UNIQUE INDEX 'uk_origin_src(filename)' ON origin_src(filename);
CREATE INDEX 'idx_origin_src(content_frag_type)' ON origin_src(content_frag_type);
