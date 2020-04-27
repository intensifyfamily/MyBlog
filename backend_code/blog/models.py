from django.db import models
from django.conf import  settings
# Create your models here.

class BaseModel(models.Model):
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Tags(BaseModel):
    type = models.CharField(max_length=10)
    content = models.CharField(max_length=20)

    class Meta:
        db_table='tags'
        verbose_name='标签'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.content


class Articles(BaseModel):
    title = models.CharField(max_length=255)
    view = models.IntegerField()
    like = models.IntegerField()
    content = models.TextField()
    tags = models.ManyToManyField(
        to='Tags',
        db_constraint=True,
        related_name='tag_article'
    )

    author = models.ForeignKey(
        to='users.UserInfo',
        db_constraint=False,
        related_name='author_article',
        on_delete=models.DO_NOTHING,
    )

    @property
    def author_name(self):
        return self.author.username

    @property
    def tag_list(self):
        return self.tags.values('id', 'type','content').all()


    class Meta:
        db_table='articles'
        verbose_name='博文'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title

class InitialComment(BaseModel):
    content = models.CharField(max_length=64)
    article = models.ForeignKey(
        to='Articles',
        db_constraint=False,
        related_name='article_icomment',
        on_delete=models.DO_NOTHING,
    )
    commentator = models.ForeignKey(
        to='users.UserInfo',
        db_constraint=False,
        related_name='commentator_icomment',
        on_delete=models.DO_NOTHING,
    )

    @property
    def commentator_name(self):
        return self.commentator.username

    @property
    def commentator_avatar(self):
        return '%s%s%s' % (r'http://127.0.0.1:8000', settings.MEDIA_URL, str(self.commentator.avatar))

    # @property
    def children(self):
        query = self.icomment_fcomment.values('id', 'content', 'commentator__username', 'commentator__avatar', 'create_time').all()
        fcomment_list = []
        for item in query:
            itemDict = {
                'id': item['id'],
                'content': item['content'],
                'username': item['commentator__username'],
                'avatar': '%s%s%s' % (r'http://127.0.0.1:8000', settings.MEDIA_URL, str(item['commentator__avatar'])),
                'create_time': item['create_time']
            }
            fcomment_list.append(itemDict)

        return fcomment_list

    class Meta:
        db_table='initial_comment'
        verbose_name='评论'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.content

class FollowUpComment(BaseModel):
    content = models.CharField(max_length=64)
    commentator = models.ForeignKey(
        to='users.UserInfo',
        db_constraint=False,
        related_name='commentator_fcomment',
        on_delete=models.DO_NOTHING,
    )
    initialcomment = models.ForeignKey(
        to='InitialComment',
        db_constraint=False,
        related_name='icomment_fcomment',
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        db_table='follow_up_comment'
        verbose_name='回复'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.content



