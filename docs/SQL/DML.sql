SELECT post.*,
       COALESCE(u1.id, u2.id)             AS u_id,
       COALESCE(u1.username, u2.username) AS u_username,
       COALESCE(u1.nickname, u2.nickname) AS u_nickname,
       COALESCE(u1.portrait, u2.portrait) AS u_portrait
FROM post
         LEFT JOIN user u1 ON post.author_id = u1.id
         LEFT JOIN user u2 ON post.author_id IS NULL AND post.portrait = u2.portrait;



DELETE
FROM user
WHERE NOT EXISTS (SELECT 1 FROM post WHERE post.author_id = user.id)
  AND NOT EXISTS (SELECT 1 FROM post WHERE post.reply_to_id = user.id)
  AND NOT EXISTS (SELECT 1 FROM at_user WHERE at_user.uid = user.id);




DELETE
FROM user
WHERE id IN (SELECT id
             FROM user u
             WHERE NOT EXISTS (SELECT 1 FROM post WHERE post.author_id = u.id)
               AND NOT EXISTS (SELECT 1 FROM post WHERE post.reply_to_id = u.id)
               AND NOT EXISTS (SELECT 1 FROM at_user WHERE at_user.uid = u.id)
    LIMIT 1000
    );