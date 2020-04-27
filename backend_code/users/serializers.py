from rest_framework import serializers
from django.conf import settings

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    motto = serializers.CharField()
    github = serializers.URLField()

    sex = serializers.SerializerMethodField()
    def get_sex(self, obj):
        return obj.get_sex_display()

    avatar = serializers.SerializerMethodField()
    def get_avatar(self, obj):
        return '%s%s%s' % (r'http://127.0.0.1:8000', settings.MEDIA_URL, str(obj.avatar))
