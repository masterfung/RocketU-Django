Post.objects.create(title='Who is the best man?', body='The one inside is the best!', author_id=2)



Comment.objects.create(text='Wow. I cannot believe this is so good. I will be a frequent visit.', posts_id=1, user_id=2)
Comment.objects.create(text='I am inspired by you!', posts_id=3, user_id=1)
Comment.objects.create(text='Congrats on your first blog', posts_id=1, user_id=3)
Comment.objects.create(text='OMG I love cheese', posts_id=4, user_id=3)
