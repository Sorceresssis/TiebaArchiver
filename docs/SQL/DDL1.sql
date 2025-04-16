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
    contents         TEXT               NOT NULL, -- json [{ type: 1, }]
    floor            INTEGER            NOT NULL, -- 楼序号，post 与其 subpost floor 相同

    agree            INTEGER DEFAULT 0  NOT NULL,
    disagree         INTEGER DEFAULT 0  NOT NULL,
    create_time      INTEGER            NOT NULL,
    is_thread_author BOOLEAN DEFAULT 0  NOT NULL, -- 楼主发的post

    sign             TEXT    DEFAULT '' NOT NULL, -- post独有. 小尾巴，原本是支持图片的，在web端可以正常显示.
    reply_num        INTEGER DEFAULT 0  NOT NULL, -- post独有. 被回复的次数.

    parent_id        INTEGER DEFAULT 0  NOT NULL, -- subpost独有, 区分 post和 subpost 的唯一标识
    reply_to_id      INTEGER DEFAULT 0  NOT NULL, -- subpost独有，表示回复的用户不是回复的subpost, 因此贴吧帖子不是树状结构。
    thread_id        INTEGER            NOT NULL,
    author_id        INTEGER            NOT NULL,

    batch            INTEGER            NOT NULL,
    update_batch     INTEGER DEFAULT 0  NOT NULL
);
CREATE INDEX 'idx_post(floor)' ON post (floor);
CREATE INDEX 'idx_post(user_id)' ON post (user_id);
CREATE INDEX 'idx_post(agree)' ON post (agree);
CREATE INDEX 'idx_post(create_time)' ON post (create_time);
CREATE INDEX 'idx_post(is_thread_author)' ON post (is_thread_author);
CREATE INDEX 'idx_post(parent_id)' ON post (parent_id);
CREATE INDEX 'idx_post(scrape_batch_id)' ON post (scrape_batch_id);


DROP TABLE IF EXISTS thread;
CREATE TABLE thread
(
    id           INTEGER PRIMARY KEY,
    title        TEXT               NOT NULL,
    contents     TEXT               NOT NULL, -- floor1
    type         INTEGER DEFAULT 0  NOT NULL,
    is_share     BOOLEAN DEFAULT 0  NOT NULL,
    is_help      BOOLEAN DEFAULT 0  NOT NULL,
    vote_info    TEXT    DEFAULT '' NOT NULL, -- json, options.length 判断是否有投票
    share_origin INTEGER DEFAULT 0  NOT NULL,
    view_num     INTEGER DEFAULT 0  NOT NULL,
    reply_num    INTEGER DEFAULT 0  NOT NULL,
    share_num    INTEGER DEFAULT 0  NOT NULL,
    agree        INTEGER DEFAULT 0  NOT NULL,
    disagree     INTEGER DEFAULT 0  NOT NULL,
    create_time  INTEGER            NOT NULL,

    forum_id     INTEGER            NOT NULL,
    post_id      INTEGER            NOT NULL, -- 首楼回复pid
    author_id    INTEGER            NOT NULL,

    status       INTEGER DEFAULT 0  NOT NULL  -- 0 正常, 1 已被屏蔽或删除
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
    id         INTEGER DEFAULT NULL NULL,     -- 古早ip用户只有 portrait, 没有 user_id， 不能设置为主键。
    portrait   TEXT    DEFAULT NULL NULL,     -- portrait按理讲是一定存在的。但是获取FragAT用户可能已无法正常查询到数据，进而无法获取到protrait。
    tieba_uid  INTEGER DEFAULT NULL NULL,     -- 老用户可能没有tieba_uid(get_userinfo)
    username   TEXT    DEFAULT ''   NOT NULL, -- 不是所有用户都有，而且爬取到的是经过脱敏的用户名
    nickname   TEXT    DEFAULT ''   NOT NULL, -- nick_name_new > nickname_old

    glevel     INTEGER DEFAULT 0    NOT NULL, -- 成长等级
    gender     INTEGER DEFAULT 0    NOT NULL, -- 0 unknown, 1 male, 2 female
    ip         TEXT    DEFAULT ''   NOT NULL,
    is_vip     BOOLEAN DEFAULT 0    NOT NULL, -- 是贵族
    is_god     BOOLEAN DEFAULT 0    NOT NULL, -- 是大神
    age        FLOAT   DEFAULT 0    NOT NULL, -- 吧龄(get_userinfo)
    sign       TEXT    DEFAULT ''   NOT NULL, -- 小尾巴(get_userinfo)
    post_num   INTEGER DEFAULT 0    NOT NULL, -- (get_userinfo)
    agree_num  INTEGER DEFAULT 0    NOT NULL, -- 被赞同数(get_userinfo)
    fan_num    INTEGER DEFAULT 0    NOT NULL, -- 粉丝数(get_userinfo)
    follow_num INTEGER DEFAULT 0    NOT NULL, -- 关注数(get_userinfo)
    forum_num  INTEGER DEFAULT 0    NOT NULL, -- 关注贴吧数(get_userinfo)

    -- 吧相关
    level      INTEGER DEFAULT 0    NOT NULL, -- 在当前吧的等级
    is_bawu    BOOLEAN DEFAULT 0    NOT NULL, -- 是吧务

    -- archive
    avatar     TEXT    DEFAULT ''   NOT NULL, -- 头像文件名
    status     INTEGER DEFAULT 0    NOT NULL, -- 0 正常, 1 查询失败 get_userinfo的查询状态
    batch      INTEGER              NOT NULL  -- 放弃了更新用户信息这个功能，需要时间来
);
CREATE UNIQUE INDEX 'uk_user(id)' ON 'user' (id);
CREATE UNIQUE INDEX 'uk_user(portrait)' ON 'user' (portrait);
CREATE UNIQUE INDEX 'uk_user(tieba_uid)' ON 'user' (tieba_uid);

DROP TABLE IF EXISTS tieba_origin_src;
CREATE TABLE tieba_origin_src
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    filename   TEXT    NOT NULL,
    origin_src TEXT    NOT NULL,
    type       INTEGER NOT NULL
);
CREATE UNIQUE INDEX 'uk_tieba_origin_src(filename)' ON tieba_origin_src (filename);
CREATE INDEX 'idx_tieba_origin_src(type)' ON tieba_origin_src (type);


