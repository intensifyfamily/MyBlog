from rest_framework.views import APIView
from utils.response import MyResponse
from . import  models, serializers
import json
# Create your views here.

class ToDo(APIView):

    def get(self, request):
        todo_obj = models.ToDo.objects.all()
        todo_ser = serializers.ToDoSerializer(todo_obj, many=True)
        results = todo_ser.data
        return MyResponse(results=results)
    def post(self, request):
        request_data = request.data
        todo_ser = serializers.ToDoDeSerializer(data=request_data)
        todo_ser.is_valid(raise_exception=True)
        todo_ser.save()
        return MyResponse()
    def put(self, request):
        request_data = request.data
        todo_obj = models.ToDo.objects.get(id=request_data['id'])
        todo_ser = serializers.ToDoDeSerializer(instance=todo_obj, data=request_data)
        todo_ser.is_valid(raise_exception=True)
        todo_ser.save()
        return MyResponse()


class ToDoDelete (APIView):

    def get(self, request, *args, **kwargs):
        todo_obj = models.ToDo.objects.filter(id=int(kwargs.get('id'))).delete()
        return MyResponse()
