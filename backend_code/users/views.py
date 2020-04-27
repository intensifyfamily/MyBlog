from utils.response import MyResponse
# data_status=200, data_msg='ok', results=None, http_status=None, headers=None, exception=False
from rest_framework.views import APIView
from . import models, serializers
# Create your views here.
class UserInfo(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.avatar = None
        self.username = None

    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        user_obj = models.UserInfo.objects.get(id=userId)
        user_ser = serializers.UserSerializer(user_obj)
        return MyResponse(results=user_ser.data)

