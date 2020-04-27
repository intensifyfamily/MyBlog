from rest_framework.serializers import ModelSerializer
from . import models

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = models.Articles
        fields = ('id', 'title', 'view', 'like', 'content', 'create_time', 'author_name', 'tag_list')

class CommentSerializer(ModelSerializer):
    class Meta:
        model = models.InitialComment
        fields = ('id', 'commentator_name', 'commentator_avatar', 'content', 'children', 'create_time')


class CommentDeSerializer(ModelSerializer):

    class Meta:
        model = models.InitialComment
        fields = ('content', 'article', 'commentator')
        extra_kwargs = {
            'content': {
                'required': True,
                'min_length': 1,
                'error_messages': {
                    'required': '必填项',
                    'min_length': '太短',
                }
            },
            'article': {
                'required': True
            },
            'commentator': {
                'required': True
            }
        }

    # # 局部钩子校验单个字段  validate_字段名
    # def validate_name(self, value):  # value是字段name的值
    #     # 书名不能包含 g 字符
    #     if 'g' in value.lower():
    #         raise ValidationError('该g书不能出版')
    #     return value
    #
    # # 全局钩子
    # def validate(self, attrs):
        # publish = attrs.get('publish')  # publish如果是外键字段，这个就是publish对象
        # name = attrs.get('name')
        # if models.Book.objects.filter(name=name, publish=publish):
        #     raise ValidationError({'book': '该书已存在'})
        # return attrs

class ReplyDeSerializer(ModelSerializer):

    class Meta:
        model = models.FollowUpComment
        fields = ('content', 'initialcomment', 'commentator')
        extra_kwargs = {
            'content': {
                'required': True,
                'min_length': 1,
                'error_messages': {
                    'required': '必填项',
                    'min_length': '太短',
                }
            },
            'initialcomment': {
                'required': True
            },
            'commentator': {
                'required': True
            }
        }
