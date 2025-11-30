---
title: 百度贴吧笔记
---

<link rel="stylesheet" href="./style/enhance.css">
<link rel="stylesheet" href="./style/custom-component.css">
<link rel="stylesheet" href="./style/reader-adapt.css">

# 百度贴吧笔记

## 数据兼容性

有些旧数据只能在 web 端正确显示。有些新数据只能在移动设备上正确显示。

## Form (吧)

一个围绕特定主题建立的讨论区

### 基本属性

| 字段         | 描述                         |
| :----------- | :--------------------------- |
| id           | 吧 id                        |
| name         | 吧名                         |
| category     | 一级分类(first_class)        |
| subcategory  | 二级分类(second_class)       |
| member_num   | 吧会员数                     |
| post_num     | 发帖量                       |
| thread_num   | 主题帖数                     |
| slogan       | 吧标语                       |
| avatar       | 吧头像(avatar/avatar_origin) |
| keyword      | 吧关键词                     |
| intro        | 简介                         |
| detail_intro | 详细简介                     |

### 板块分区

吧管理员可以创建

? 如果原来的板块删除，该板块的帖子会怎么样？

### 友情贴吧

友情贴吧是百度贴吧推出的官方跨吧互动工具，方便百度贴吧使用者找到自己感兴趣的话题的连接功能

> 柯南吧的友情贴吧
>
> ![1762792490992](./.assets/note_analysis_tieba/images/1762792490992.png)

```jsonc
// aiotieba get_tieba body
{
  // ...
  "friend_forum": [
    {
      "forum_name": "新孙笑川",
      "forum_id": 27400819,
      "avatar": "http://tiebapic.baidu.com/forum/w%3D120%3Bh%3D120/sign=09975b648c177f3e1034f80f40f453fa/267f9e2f07082838c76f15c6fd99a9014d08f187.jpg?tbpicau=2025-11-13-05_ca8da6607abcc48b51b9387f4e628866"
    }
  ]
}
```

### 吧图片 [Web 端]

**※ 吧图片区**

吧图片板块是由多个相册组成，可以给相册设置分类。

![1762706744103](./.assets/note_analysis_tieba/images/1762706744103.png)

**※ 相册内部**

相册内部的上半部分是图片区

![1762706559810](./.assets/note_analysis_tieba/images/1762706559810.png)

下半部分与主题帖结构相同，相册对应的 url 结构也与主题帖相同。可以认为吧相册是一个 `带有图片区的特殊主题帖`

![1762709335255](./.assets/note_analysis_tieba/images/1762709335255.png)

**※ 移动端显示**

由于移动端没有适配相册，所以移动端把相册当作了主题帖来显示

<img src="./.assets/note_analysis_tieba/images/1762709455730.png" alt="1762709455730" style="zoom:30%;" />

### 吧视频 [Web 端]

> 与移动端的视频模块不同，移动端的视频模块展示的是视频主题帖里的视频。

**吧视频区**

![1762710439604](./.assets/note_analysis_tieba/images/1762710439604.png)

**视频专辑**

![1762710507504](./.assets/note_analysis_tieba/images/1762710507504.png)

### 吧刊 [Web 端][功能已下线]

2010 年推出的电子杂志平台,

吧刊有背景音乐，背景，和其他多媒体元素。

> [百度百科-吧刊](https://baike.baidu.com/item/%E5%90%A7%E5%88%8A)

### 吧聊天频道

![1763234363131](./.assets/note_analysis_tieba/images/1763234363131.png)

![1763234357507](./.assets/note_analysis_tieba/images/1763234357507.png)

### 吧 AI

#### AI 智能体

用户创建的 AI 聊天机器人，可以给它设置特定的属性和身份。它可以看作是一种特殊的用户, 拥有部分的用户特性。在 [Thread](<#thread-(主题帖)>) 中可以被 @，这些 AI 智能体也会回复你的消息。

![1763233983752](./.assets/note_analysis_tieba/images/1763233983752.png)

#### AI 游戏

通过与 AI 智能体进行文字对话进行的游戏。得到足够的分数即可获胜。

![1763233590490](./.assets/note_analysis_tieba/images/1763233590490.png)

**创建 AI 游戏**

先选择一位 AI 智能体，写下各种游戏设定就可以创建 AI 游戏了。

![1763233884332](./.assets/note_analysis_tieba/images/1763233884332.png)

### 吧管理

#### 吧务

> [百度百科-吧主](https://baike.baidu.com/item/%E5%90%A7%E4%B8%BB)

**大吧主**

大吧主是各贴吧的最高权限管理者

- 大吧主可将 ID 在所属贴吧内封禁 1/3/10 天（到期后自动解封）。
- 大吧主有解封权限（在吧务后台解封），小吧主没有解封权限。
- 大吧主可以将部分吧友加入黑名单。
- 大吧主可以删贴，也可以置顶或加精贴子。

**小吧主**

小吧主以辅助大吧主管理贴吧为主，主要权限为封禁 ID 一天、删贴等。

**职业吧主**

职业吧主是指有职业化素养，有职业技能水准的吧主。由贴吧官方邀请或满足相应条件的大吧主可申请职业吧主。

**官方吧主(第四吧主)**

官方吧主是通过贴吧企业平台吧认证的吧主，属于官方人员，负责监视贴吧和及时提供便捷信息。

**语音小编**

百度贴吧于 2013 年推出语音功能后，新增的一项贴吧职务。主要职责是引导吧内语音相关内容建设，开展积极向上的语音活动，参与语音贴的审核管理。

> [百度百科-语音小编](https://baike.baidu.com/item/%E8%AF%AD%E9%9F%B3%E5%B0%8F%E7%BC%96)

**图片小编**

管理贴吧图片库

> [百度百科-图片小编](https://baike.baidu.com/item/%E5%9B%BE%E7%89%87%E5%B0%8F%E7%BC%96)

**视频小编**

管理贴吧视频库

> [百度百科-视频小编](https://baike.baidu.com/item/%E8%A7%86%E9%A2%91%E5%B0%8F%E7%BC%96)

**广播小编**

管理贴吧广播

**吧刊主编**

管理吧刊

**吧刊小编**

管理吧刊

<!-- TODO 吧务日志 -->

#### 吧规

### 个性配置

**吧背景**

移动端和 web 端不互通，要单独设置。

```jsonc
// aiotieba get_tieba body 移动端 Banner 图片
{
  // ...
  "activityhead": {
    "head_imgs": [
      {
        "img_url": "http://tiebapic.baidu.com/forum/q%3D80%26w%3D644/sign=5bbfb2c33dcb0a46832286394d14cb12/8326cffc1e178a82ee4d2f99b003738da977e892.jpg?tbpicau=2025-11-13-05_714557382ab16fc35a9248fc63e4724c",
        "type": 1
      }
    ]
  }
}
```

### 待处理

吧广播
吧活动
语音频道
互动抽奖
小卖铺
板块分区

置顶，精品帖

## Thread (主题帖)

### 基本属性

| 字段         | 描述               |
| :----------- | :----------------- |
| id           | 主题帖 id          |
| title        | 标题               |
| forum        | 所属吧相关信息     |
| thread_type  | 帖子类型           |
| post_id      | 首帖 id            |
| author       | 主题帖作者相关信息 |
| is_shared    | 是否为分享帖       |
| share_origin | 分享来源帖         |
| is_help      | 是否为求助帖       |
| tab_id       | 板块分区 id        |
| vote_info    | 投票信息           |
| view_num     | 浏览量             |
| reply_num    | 回复数             |
| share_num    | 分享数             |
| agree        | 赞数               |
| disagree     | 踩数               |
| create_time  | 创建时间           |
| last_time    | 最后更新时间       |

#### 投票

```json
{
  "vote_info": {
    "title": "t",
    "is_multi": false,
    "options": [
      {
        "vote_num": 1488,
        "text": "t1"
      },
      {
        "vote_num": 304,
        "text": "t2"
      }
    ],
    "total_vote": 1792,
    "total_user": 1792
  }
}
```

#### 帖子属性

| 字段     | 属性     |
| :------- | :------- |
| is_share | 是分享帖 |
| is_help  | 是求助帖 |
| is_top   | 置顶     |
| is_good  | 精华帖   |

设置为置顶和精华帖是吧管理员操作。

#### 内容声明

1. 帖子原创声明
2. 帖子含 AI 内容

#### AI 智能体

可以给主题帖添加多个 AI 智能体。没有其他的作用，就只是展示。

![1764508852037](./.assets/note_analysis_tieba/images/1764508852037.png)

#### 首帖

首帖(first post), 主题帖的正文就在首帖中。主题帖的 `话题` 也作为一个内容分块保存在首帖中。

在客户端首帖相比其他的回复帖会有特殊的展示样式。比如百度网盘等应用的链接会识别为卡片

### 帖子类型

字段 `thread_type` 标识帖子类型，不同类型的帖子有不同的功能和展示形式。

|  帖子类型  | thread_type | 属性字段        | 介绍                                     |
| :--------: | :---------: | :-------------- | :--------------------------------------- |
| 文章/图文  |      0      |                 | 普通主题帖                               |
|   转发帖   |      0      | is_share        | 有转发引用的普通主题帖                   |
|   求助贴   |      0      | is_help         | 有 "求助" 标签的普通主题帖               |
|   相册帖   |      1      |                 | [吧图片相册](#吧图片-[web-端])对应的帖子 |
|   语音帖   |     11      | is_voice_thread | 首帖有语音的主题帖                       |
| 会员小说帖 |     31      |                 | "短故事" 模块的付费小说贴                |
|   视频帖   |     40      |                 | 首帖有视频的主题帖                       |
|   直播贴   |     50      |                 | ALA 直播                                 |
|   打分帖   |     75      |                 | 可以打分的帖子                           |
|   抽奖贴   |     76      |                 | 由吧管理员发起的抽奖帖                   |

> 百度贴吧发布主题贴时无法同时发送语音和视频因此不需要考虑类型冲突。

#### 分享帖/转发帖

**※ 介绍**

转发贴是引用转发其他帖子的帖子，可以添加一些自己的评论，和微博的转发类似。

> `转发贴无法作为被引用转发的对象`。举个例子：转发贴 T2 是引用转发 T1 的转发贴，当引用转发 T2 时，生成的新转发贴 T3 实际上引用转发的是 T1，而不是 T2。不论转发多少次，最终引用转发的都是最初的帖子。

**※ 可选功能**

- 首帖可以输入 `文字`、`emoji`、`@用户`
- 选择（单选）分享到什么吧的什么板块分区
- 可添加话题

#### 会员小说贴

**※ 介绍**

会员小说贴是百度贴吧推出的付费小说。这种帖子主要存在于小说和故事类的吧。

```
10134038937
8791942255
```

![1764109704953](./.assets/note_analysis_tieba/images/1764109704953.png)

#### 打分帖

**发帖**

3. 先选择 n(n>=3)个图片，然后裁切成符合要求的尺寸。贴吧根据图片自动生成 n 个打分项。
4. 给每打分项填入 `名称`(必填) 和 `补充简介` 。
5. 无法添加 `视频` ，`语音` ，`投票`
6. 可以设置打分权限，所有人 or 吧等级选择

**打分和评论**

![1764443267435](./.assets/note_analysis_tieba/images/1764443267435.png)

可以多次打分，每次评论都附上打分情况。但是评论的打分不会跟着打分跟新而跟新

![1764443398579](./.assets/note_analysis_tieba/images/1764443398579.png)

#### 抽奖贴

1. 无法添加 `视频` ，`语音` ，`投票`
2. 添加奖项，最多三个。设置奖品封面，名称，数量（<100），价值（单个不超过 5 万元）
3. 设置抽奖参与范围限，1.所有人。 2.吧等级选择
4. 设置参与方式：1.评论字数大于等于 x; 2.带上设置的关键词
5. 设置领奖有效期

```json
{
  "draw_info": {
    "marquee_info": {
      "intro": "1位吧友已中奖",
      "user_list": [
        {
          "portrait": "tb.1.b50d4847.i51xEvI66eY-Ubg52AmBGw",
          "nickname": "Lovely薬草儿",
          "suffix": "抽中了天才"
        }
      ]
    },
    "prize_list": [
      {
        "name": "猪头",
        "pic": "https://tiebapic.baidu.com/tieba/pic/item/37d12f2eb9389b5014ef364ac335e5dde7116e92.jpg?tbpicau=2025-12-12-05_c2d3ccd8f26fa1981afeac473de1d162",
        "count": 5
      },
      {
        "name": "小狗",
        "pic": "https://tiebapic.baidu.com/tieba/pic/item/a8ec8a13632762d0f42c72a7e6ec08fa513dc69c.jpg?tbpicau=2025-12-12-05_51fef1850224c97e36ef75105f57fade",
        "count": 1
      },
      {
        "name": "天才",
        "pic": "https://tiebapic.baidu.com/tieba/pic/item/377adab44aed2e736cfb5034c101a18b87d6fa9d.jpg?tbpicau=2025-12-12-05_65340bdcc6edf72823c46018314efd3b",
        "count": 6
      }
    ],
    "countdown": {
      "intro": "本活动已结束",
      "btn_info": {
        "text": "查看中奖结果",
        "url": "https://tieba.baidu.com/mo/q/hybrid-main-pb/prizeResult?thread_id=10227773769\u0026customfullscreen=1\u0026nonavigationbar=1\u0026loadingSignal=1"
      }
    },
    "audit_status": 1,
    "open_status": 3,
    "lottery_type": 1
  }
}
```

### 管理

- 吧务团队删帖
- 系统删帖
- 楼主删帖
- 自己删帖
- 其他删帖

#### 评论范围

#### 编辑/删除回复

编辑首帖

### 贴吧 API

获取帖子的 API

获取 可以获取到分区。

## Post (回复贴/楼)

### 基本属性

| 字段  | 描述    |
| :---- | :------ |
| id    | 回复 id |
| floor | 设备    |

#### IP

#### 设备 [Web 端]

#### 签名档 [Web 端][功能已下线]

带有图片的

#### 签名/小尾巴 [移动端]

随着 post 发布的 sign 不会随着用户修改而改变。

结构和 post/subpost 的 content

```python
# signature = List[Content]

signature
{
  content
{
  text: "S：小B,你知道世上最难的事是什么吗？"
}
content
{
  type: 2
  text: "image_emoticon25"
}
content
{
  text: "\nB：毁灭世界？"
}
content
{
  type: 2
  text: "image_emoticon15"
}
content
{
  text: "\nS：错，是山海十连出金！！"
}
content
{
  type: 2
  text: "image_emoticon16"
}
}
```

#### 回复数

删除楼中楼，不会减少 reply_num 的值。只会一只增加。

更新 archive 时，记得更新 reply_num。

### 申请恢复

### 重新编辑

### 接口返回数据错误

**※ **

## Subpost (子回复/楼中楼)

subpost 是 post 的回复。subpost 的结构与 post 较为相似。

### 基本属性

| 字段        | 区分 Post | 描述              |
| :---------- | :-------- | :---------------- |
| parent_id   | Subpost   | 回复对象的 postId |
| reply_to_id | Subpost   | 回复对象的 userId |

#### 回复对象

贴吧 subpost 的回复对象指向的是用户，不是帖子。所以它不是像 reddit 一样的树形结构。

贴吧的历史包袱很大，回复对象有多种表示方式。

**※ 回复对象的多种表示方式**

1. 回复对象作为 `文本分块` 直接嵌入在帖子的内容中

```json
contents: [
  {
    text: "回复 "
  },
  // 文本分块
  {
    text: "$nickname"
  },
  {
    text: "："
  },
  {
    text: "...正文..."
  }
]
```

2. 回复对象作为 `at 分块` 嵌入在帖子的内容中

不过需要注意的是很多表示回复对象的 at 分块的 user_id 是 `空值`，并不能通过 user_id 去定位用户。

```json
contents: [
  {
    text: "回复 "
  },
  // at 分块
  {
    text: "$nickname"
    user_id: 0
  },
  {
    text: "："
  },
  {
    text: "...正文..."
  }
]
```

3. 使用 reply_to_id 字段表示回复对象

目前官方使用的是这个方法。

**※ 回复对象的错误显示实例**

1. 保存错误

```
tid:9003722572
floor:10
pid:150220952214
spid:150228714442
```

![1763927271940](./.assets/note_analysis_tieba/images/1763927271940.png)

2. 多种表示方式冲突

![1763928221276](./.assets/note_analysis_tieba/images/1763928221276.png)

## Content (内容)

### 编号

```python
# From: aiotieba

_type = proto.type
# 0纯文本 9电话号 18话题 27百科词条
if _type in [0, 9, 18, 27]:
  frag = FragText_pt.from_tbdata(proto)
  texts.append(frag)
  yield frag
# 11:tid=5047676428
elif _type in [2, 11]:
  frag = FragEmoji_pt.from_tbdata(proto)
  emojis.append(frag)
  yield frag
elif _type == 4:
  frag = FragAt_pt.from_tbdata(proto)
  ats.append(frag)
  texts.append(frag)
  yield frag
elif _type == 1:
  frag = FragLink_pt.from_tbdata(proto)
  links.append(frag)
  texts.append(frag)
  yield frag
# 35|36:tid=7769728331 / 37:tid=7760184147
elif _type in [35, 36, 37]:
  frag = FragTiebaPlus_pt.from_tbdata(proto)
  tiebapluses.append(frag)
  texts.append(frag)
  yield frag
# outdated tiebaplus
elif _type == 34:
  continue
else:
  yield FragUnknown.from_tbdata(proto)
```

### 表情分块

```c#
const emoticonsIndex = {
  image_emoticon: { class: 'client', ext: 'png' }, // 泡泡(<51)/客户端新版表情(>61)
  // image_emoticon: { class: 'face', ext: 'gif', prefix: 'i_f' }, // 旧版泡泡
  'image_emoticon>51': { class: 'face', ext: 'gif', prefix: 'i_f' }, // 泡泡-贴吧十周年(51>=i<=61)
  bearchildren_: { class: 'bearchildren', ext: 'gif' }, // 贴吧熊孩子
  tiexing_: { class: 'tiexing', ext: 'gif' }, // 痒小贱
  ali_: { class: 'ali', ext: 'gif' }, // 阿狸
  llb_: { class: 'luoluobu', ext: 'gif' }, // 罗罗布
  b: { class: 'qpx_n', ext: 'gif' }, // 气泡熊
  xyj_: { class: 'xyj', ext: 'gif' }, // 小幺鸡
  ltn_: { class: 'lt', ext: 'gif' }, // 冷兔
  bfmn_: { class: 'bfmn', ext: 'gif' }, // 白发魔女
  pczxh_: { class: 'zxh', ext: 'gif' }, // 张小盒
  t_: { class: 'tsj', ext: 'gif' }, // 兔斯基
  wdj_: { class: 'wdj', ext: 'png' }, // 豌豆荚
  lxs_: { class: 'lxs', ext: 'gif' }, // 冷先森
  B_: { class: 'bobo', ext: 'gif' }, // 波波
  yz_: { class: 'shadow', ext: 'gif' }, // 影子
  w_: { class: 'ldw', ext: 'gif' }, // 绿豆蛙
  '10th_': { class: '10th', ext: 'gif' } // 贴吧十周年
} as const;
```

### 新表情

```json
// tid: 5047676428; pid:105717733306; floor:1
{
  "type": 11,
  "c": "新表情",
  "width": 160,
  "height": 160
}
```

```json
{
  "pid": "105718545127",
  "spid": "105720148087",
  "user_name": "偶尔也会动",
  "portrait": "tb.1.d240f580.xZrQ8WoKJCsbMMHSm-0nmQ",
  "showname": "偶尔也会动",
  "user_nickname": "贴吧用户_0R9tW5U"
}
```

### AT 分块

@用户的分块，其中显示的文字显示的是 showname, 不是 username。

```json
{
  text='nickname',
  user_id=0
}
```

### 视频分块

每条贴子只能发一条视频。

```json
// aiotieba
{
  "video": {
    "src": "",
    "cover_src": "",
    "duration": 0,
    "width": 0,
    "height": 0,
    "view_num": 0
  }
}
```

```json
// raw data - 直播贴的视频
  content {
    type: 5
    text: "http://tieba.baidu.com/ala/share?live_id=528674"
    link: "http://ge1ijh7qci7i3d9d24z.exp.bcevod.com/mda-hc5s1817u7q9rdut/mda-hc5s1817u7q9rdut.mp4"
    src: "http://himg.baidu.com/sys/portraitl/item/f86ee4b880e9a297e4b880e9a297e7b1b3e7b2926564.jpg"
    bsize: "200,200"
    during_time: 1704
    width: 200
    height: 200
    count: 1364
  }
```

### 语音分块

每条 Post/Subpost 只能发送一条语音

```json
{
  "voice": {
    "md5": "",
    "duration": 0
  }
}
```

语音下载地址

```
https://tiebac.baidu.com/c/p/voice?voice_md5=$voice_md5&play_from=pb_voice_play
```

### 图片分块

自定义填字表情包

### 链接分块

部分链接会被解析为卡片

### 话题分块

话题是纯文本。用##包裹，

用百度的 api 去搜索。

### tiebaplus 分块

### 待处理

自定义填字表情包

话题

## User (用户)

AI 用户
portrait

### 基本属性

| 属性      | 说明   |
| --------- | ------ |
| show_name | 显示名 |
| portrait  | 头像   |
| sign      | 签名   |
| ip        | 性别   |

### IP

贴吧不是每个帖子都保存发布时的 ip 地址。会随着用户的 ip 改变

有些没有一直没登陆的用户爬不出 ip。

### 用户标识

**user_id**

可能为空，上古 ip 用户没有 user_id.

user_id 可能不存在

`https://github.com/Starry-OvO/aiotieba/issues/213#issuecomment-2241636224`

**portrait**

一定不为空, 很重要的参数。

有多个版本。

**username**

可能为空，早期互联网需要填写用户名。但是现在很多账号没有用户名。

post 会保存一些关于用户的冗余字段。会保留一些被 `-` 代替的用户名。

接口请求到的 username 是经过处理的。

1. 电话号码类

电话号码会被隐私处理: `133******37`

```json
{
  "user_id": 1371763488,
  "portrait": "tb.1.e67e027b.vYbye7MZFu33wtZGvHLLdg",
  "user_name": "-",
  "nick_name_new": "璐村惂鐢ㄦ埛_QA3J3KS馃惥",
  "tieba_uid": 0,
  "glevel": 0,
  "gender": 1,
  "age": 9.9,
  "post_num": 1304,
  "agree_num": 0,
  "fan_num": 29,
  "follow_num": 15,
  "forum_num": 108,
  "sign": "新生的BIGER",
  "ip": "",
  "icons": ["wxshen", "wxxian", "wxyao"],
  "vimage": {
    "enabled": false,
    "state": ""
  },
  "is_vip": false,
  "is_god": false,
  "is_blocked": false,
  "priv_like": 3,
  "priv_reply": 1
}
```

2. 敏感字, 会被用 `-` 符号代替。

`你麻痹972`

```json
{
  "user_id": 1164702015,
  "portrait": "tb.1.8b4d3d91.a4jtPwNaT61v33tAzAFOTA",
  "user_name": "-",
  "nick_name_new": "贴吧用户_Q7Me34C",
  "tieba_uid": 0,
  "glevel": 0,
  "gender": 1,
  "age": 9.2,
  "post_num": 2612,
  "agree_num": 6,
  "fan_num": 85,
  "follow_num": 12,
  "forum_num": 9,
  "sign": "怪我咯。",
  "ip": "",
  "icons": [],
  "vimage": {
    "enabled": false,
    "state": ""
  },
  "is_vip": false,
  "is_god": false,
  "is_blocked": false,
  "priv_like": 3,
  "priv_reply": 1
}
```

`X1NPJ`

```json
{
  "user_id": 1604997478,
  "portrait": "tb.1.726db229.anu5OjnVZiPVETH8_E6VQg",
  "user_name": "-",
  "nick_name_new": "万志翔",
  "tieba_uid": 1134632183,
  "glevel": 2,
  "gender": 1,
  "age": 9.4,
  "post_num": 1233,
  "agree_num": 715,
  "fan_num": 0,
  "follow_num": 0,
  "forum_num": 0,
  "sign": "",
  "ip": "内蒙古",
  "icons": [],
  "vimage": {
    "enabled": false,
    "state": ""
  },
  "is_vip": false,
  "is_god": false,
  "is_blocked": false,
  "priv_like": 1,
  "priv_reply": 1
}
```

`贴吧用户_0002VDb🐾`

```json
{
  "user_id": 579507,
  "portrait": "tb.1.25502702.BrAM9CZAwzNgOWADvgm_JQ",
  "user_name": "-",
  "nick_name_new": "贴吧用户_0002VDb🐾",
  "tieba_uid": 10243430,
  "glevel": 0,
  "gender": 2,
  "age": 19.9,
  "post_num": 671826,
  "agree_num": 948,
  "fan_num": 48,
  "follow_num": 0,
  "forum_num": 216,
  "sign": "不同的人在用别搞混啦",
  "ip": "",
  "icons": [],
  "vimage": {
    "enabled": false,
    "state": ""
  },
  "is_vip": false,
  "is_god": false,
  "is_blocked": false,
  "priv_like": 3,
  "priv_reply": 1
}
```

`百度用户#981758301`

```json
{
  "user_id": 811989719,
  "portrait": "tb.1.e1543ca9.sIAxKFosukK97_rHsI4fKw",
  "user_name": "-",
  "nick_name_new": "璐村惂鐢ㄦ埛_0EJ1yMe馃惥",
  "tieba_uid": 0,
  "glevel": 0,
  "gender": 1,
  "age": 11.5,
  "post_num": 2768,
  "agree_num": 2,
  "fan_num": 47,
  "follow_num": 57,
  "forum_num": 28,
  "sign": "大爱六六",
  "ip": "",
  "icons": [],
  "vimage": {
    "enabled": false,
    "state": ""
  },
  "is_vip": false,
  "is_god": false,
  "is_blocked": false,
  "priv_like": 2,
  "priv_reply": 1
}
```

`贴吧用户_06y9CQW`

```json
{
  "user_id": 568818738,
  "portrait": "tb.1.66a5b431.2vB54rBhK3J7pvxZ2Mc3ng",
  "user_name": "-",
  "nick_name_new": "贴吧用户_06y9CQW",
  "tieba_uid": 37499515,
  "glevel": 0,
  "gender": 1,
  "age": 12.5,
  "post_num": 3665,
  "agree_num": 15,
  "fan_num": 43,
  "follow_num": 134,
  "forum_num": 17,
  "sign": "我就是我，不是五毛一盒的烟火，，，，，",
  "ip": "安徽",
  "icons": [],
  "vimage": {
    "enabled": false,
    "state": ""
  },
  "is_vip": false,
  "is_god": false,
  "is_blocked": false,
  "priv_like": 3,
  "priv_reply": 1
}
```

**tieba_uid**

可能为空， 也没什么用

### 签名

### 头像

目前百度贴吧移动端用 `portrait` 这一参数来请求头像图片。

```powershell
# 小头像
 # t=$timestamp 这个参数我猜测是头像修改的时间
https://gss0.baidu.com/7Ls0a8Sm2Q5IlBGlnYG/sys/portrait/item/$portrait?t=$timestamp
http://tb.himg.baidu.com/sys/portrait/item/$portrait

# 高清头像
https://himg.bdimg.com/sys/portraith/item/$portrait
```

> 要注意的是，你在网页端浏览帖子时看到的用户头像可能会与爬取到的图片不一样。因为爬取头像依靠的是
> `https://himg.bdimg.com/sys/portraith/item/$portrait` 这个接口。网页端由于其特殊的加载方式导致有些有年代的帖子会加载过时的头像（用户以前的头像）。

### level 和 glevel 的区别

level 吧内等级

glevel 贴吧成长等级

### 用户印记

## 其他功能

### 语音广场/语音频道
