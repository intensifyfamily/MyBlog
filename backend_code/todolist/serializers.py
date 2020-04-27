from rest_framework.serializers import ModelSerializer
from . import models

class ToDoSerializer(ModelSerializer):
    class Meta:
        model = models.ToDo
        fields = ('id', 'title', 'content', 'is_done', 'create_time', 'finish_time')

class ToDoDeSerializer(ModelSerializer):

    class Meta:
        model = models.ToDo
        fields = ('title', 'content', 'is_done')
        extra_kwargs = {
            'title': {
                'required': True,
                'min_length': 1,
                'error_messages': {
                    'required': '必填项',
                    'min_length': '太短',
                }
            },
            'content': {
                'required': False
            },
            'is_done': {
                'required': False
            }
        }
