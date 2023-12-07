from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


class PostList(APIView):
    def get(self, request):
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(serializer.data, status=200)
    

    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)


class PostDetail(APIView):
    def get_object(self, id):
        return get_object_or_404(Post, pk=id)
    

    def get(self, request, id):
        post = self.get_object(id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=200)
    

    def put(self, request, id):
        post = self.get_object(pk=id)
        data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=data)

        if serializer.is_valid(raise_exception=True):
            post = serializer.save()
            post.save()
            return Response(serializer.data, status=201)
        
    
    def delete(self, request, id):
        post = self.get_object(pk=id)
        post.delete()
        return Response({"msg": "Post removed"}, status=200)