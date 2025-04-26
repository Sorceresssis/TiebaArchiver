"""

https://github.com/lumina37/aiotieba/issues/261#issuecomment-2681084538


用户主页的主题帖是可以隐藏的。get_user_threads查不到被用户隐藏的主题帖。
而get_user_posts利用了一个贴吧长期存在的“漏洞接口”，使用一个8.9.8.5的版本号就能绕过上述的隐藏机制查出所有用户发帖（包括回复）。只有用户在网页端勾选上“隐藏所有动态”这个选项，上述基于“漏洞接口”的查找功能才会被屏蔽。具体实现：


"""

# 用 get_user_posts 。
# 查出所有的pos，然后根据 tid 查出对应的帖子。
#  是否存在。  是否时 author_thread

# * 可以正常打开的 thread。
# 不能正常打开的就，保存 post.


# get_user_posts 返回的只能是 FragText ，所以很多信息无法解析
# 图片会变成
# LIST: Contents_up(objs=[FragText(text='[图片]')])
# LIST: Contents_up(objs=[FragText(text='[图片]')])
# LIST: Contents_up(objs=[FragText(text='[图片]')])
# LIST: Contents_up(objs=[FragText(text='[图片]')])
# LIST: Contents_up(objs=[FragText(text='[图片]')])
# LIST: Contents_up(objs=[FragText(text='[图片]')])
# LIST: Contents_up(objs=[FragText(text='[图片]')])
# LIST: Contents_up(objs=[FragText(text='[图片]')])

# 当 出现 UserPostss(objs=[])  时不代表，就没了。


# ANCHOR
# 会出现 UserPost(contents=Contents_up(objs=[]), 但是实际上是有内容的情况。就是一切要以 thread 显示为准。
# tid 3517367868  floor: 58
