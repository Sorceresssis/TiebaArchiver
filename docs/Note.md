---
---

<link rel="stylesheet" href="https://sorceresssis.github.io/store/doc-css/enhance.css">
<link rel="stylesheet" href="https://sorceresssis.github.io/store/doc-css/custom-component.css">
<link rel="stylesheet" href="https://sorceresssis.github.io/store/doc-css/reader-adapt.css">

# 开发笔记

> 记录一下思路和需要考虑的问题。帮助自己后续程序的改进。减少思考时间。

## 备忘录

### 屏蔽的 share_origin 恢复正常后, 使用 update_archived 补齐

被屏蔽和删除的 share_origin 可能会被解封，需要有后续补齐的功能。

### user 信息处理

※ **user 来源**

1. post 的发帖人
2. subpost 的发帖人
3. subpost 的 reply_id
4. content 的 at 分块

※ **user 放在最后统一处理的原因。**

由于 archive_config.post_filter 中 有 AUTH_RPL_W_ALL / AUTH_RPL_W_AUTH 两种配置。 需要获取到所有的 subpost 后才能得知
post
否是 Thread's author Replied, 不符合需要删除掉所有的 subpost.其中 subpost 的作者也需要被删除。
如果把用户和 post 一起处理，会有很多流量和性能的浪费。
所以在处理 post 和 subpost 时只利用现有的数据向数据库登记。不进行 get_user_info() 完善数据，和下载头像的操作。

※ **在处理 post 和 subpost 时如何向数据库 user 表登记。**

由于 user 的来源多种多样，并且有重合，重要的是来源的信息完整度不一样。比如说 Aiotieba.Posts.obj[x].UserInfo_p 的信息量就比
FragAt 的信息量高（FragAt 只包含 user_id ， nickname），
所以 user 表中有一个 `completeness` 字段如何登记时发现该用户已经存在，但是完整度比目前发起的等级低，就更新改数据。
这样做的原因是：在用户已经注销的情况下可以保留残存在各个地方的冗余信息。

其中特殊的是 at 用户，需要向 `at_user` 表中在登记一次。因为 at 分块变成了 json。很难判断是否是被删除的 subpost 中 at 用户。

※ **usre 同一处理的过程**

- 要先把多余的 user 删除掉。

```sqlite
DELETE
FROM user
WHERE NOT EXISTS (SELECT 1 FROM post WHERE post.author_id = user.id)
  AND NOT EXISTS (SELECT 1 FROM post WHERE post.reply_to_id = user.id)
  AND NOT EXISTS (SELECT 1 FROM at_user WHERE at_user.uid = user.id);
```

- 然后开始查询 `done=0` 的 user 去完善。

user 表 `done` 字段的作用： 在程序意外停止后，使用程序更新功能依然能把没有完善的用户信息完善。

### 媒体文件保存规则

※ **为什么 post 的媒体文件不是先在数据库中记录映射好，到最后集中下载呢**

为了防止没有没有文件后缀名的情况，程序需要先下载才能判断文件类型。

是否有 content_type

url 是否有文件后缀名

※ **文件命名规则**

大致的规则： 文件名一定要有所属的信息。方便删除和查找。

`f@5949494_avatar` forum 的文件

`p@12346_1_58` post 的文件

`u@tb.1.xxxxx.1-xxxxx-xxx-xx` user 的文件

※ **amr 语音转换一份 mp3 的**

### post/subpost traffic 信息

如果不更新 traffic 信息会导致 post 的 reply_num 不准确。

tieba-read 应该删去 reply_num 的判断，直接向数据库中查询。

### share_origin 可能已被屏蔽或删除的处理方法

1. 被屏蔽和删除的 share_origin 可能会被解封，因此需要处理好 share_origin 解封后如何补上。

### AUTH_RPL_W_ALL / AUTH_RPL_W_AUTH 处理方法

先处理完 subposts, 如果配置是 AUTH_RPL_W_ALL / AUTH_RPL_W_AUTH，就在数据库中判断是否是 thread_author 回复过的 post。

如果不是就删除所有 subposts （batch_id），跳过这个 post。

先处理 subposts 可以免去 post 的保存和删除。

全部的 post 处理完后，再集中处理用户,
要删除没有关联的用户（就是删除 subpost 的用户）。然后才完善用户数据。

### update_archive 时修改了 post_filter 配置项处理方法

用 post 的 batch_id 字段来隔绝不同批次的影响。

### user_post 怎么保存？。

※ get_user_posts() 当连续 60 个返回的数组是空就停止。

### user thread & post 处理。

thread->get_user_threads()

thread->get_user_posts()

thread & post->get_user_posts()

```
tid: 123456789
title: dfd
status : 正常 | 丢失。  丢失后回复。 对于丢失的 threads， 是否检查一边。
regised: 已经登记到了。


遍历到 已经登记到的就 停止。
```

- 有一个时间锚点。
  thread 如何转化成 post.

? 如何处理 thread 已经被删除和屏蔽的情况。

只有 post 了 ，
残缺 post.

? 被删除的 thread 恢复后如何补齐。 查询删除的 thread。 重新检查一遍。
