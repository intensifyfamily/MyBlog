from rest_framework.views import APIView
from . import models, serializers
from utils.response import MyResponse
from datetime import datetime
# Create your views here.

class Articles(APIView):

    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        request_data = request.query_params
        if not 'articleId' in request_data:
            article_obj = models.Articles.objects.filter(author_id=userId, is_delete=False)
            article_ser = serializers.ArticleSerializer(article_obj, many=True)
        else:
            article_obj = models.Articles.objects.get(id=request_data['articleId'], is_delete=False)
            article_ser = serializers.ArticleSerializer(article_obj)
        results = article_ser.data
        for item in results:
            item['desc'] = item['content'][:20]
        return MyResponse(results=results)

class Comment(APIView):

    def get(self, request, *args, **kwargs):
        articleId = kwargs.get('articleId')
        request_data = request.query_params
        comment_obj = models.InitialComment.objects.filter(article_id=articleId, is_delete=False)
        comment_ser = serializers.CommentSerializer(comment_obj, many=True)
        results = comment_ser.data
        for r in results:
            r.update({'replyDisplay': 'none'})
        return MyResponse(data_status=200, data_msg='ok', results=results, http_status=200, headers=None, exception=None, total=len(results))

    def post(self, request, *args, **kwargs):
        articleId = kwargs.get('articleId')
        request_data = request.data
        request_data.update({"article": articleId})
        comment_ser = serializers.CommentDeSerializer(data=request_data)
        comment_ser.is_valid(raise_exception=True)
        comment_ser.save()
        return MyResponse()

class Reply(APIView):

    def post(self, request, *args, **kwargs):
        request_data = request.data
        reply_ser = serializers.ReplyDeSerializer(data=request_data)
        reply_ser.is_valid(raise_exception=True)
        reply_ser.save()
        return MyResponse()

