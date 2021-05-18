from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, generics, status, filters
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from .models import Blogs, UserImages
from .serializers import  BlogSerializer, CreateBlogSerializer, UserImageSerializer


class CreateBlogAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CreateBlogSerializer

    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        blog = serializer.save()

        return Response({
            'message': 'successfully Blog created',
            'blog': BlogSerializer(blog).data
        })

# class ImagesUploadAPI(APIView):
#     permission_classes = [ permissions.IsAuthenticated ]
#     parser_classes = [ MultiPartParser, FormParser]
#     serializer_class = UserImageSerializer

#     def post(self, request, format=None):
#         # print(request.data)
#         serializer = self.serializer_class(data=request.data)
#         print(serializer)
#         if serializer.is_valid(raise_exception=True):
#             # image = serializer.save(
#             #     user = request.user,
#             #     image = request.data.get('image')
#             # )
#             serializer.save()
#             return Response({
#                 'data': serializer.data,
#                 'message': 'image saved'
#             })
#         return Response({
#                 serializer.errors,
#             })
# @csrf_exempt 
# class ImagesUploadAPI(ViewSet):
#     permission_classes = [ permissions.IsAuthenticated ]
#     serializer_class = UserImageSerializer

#     def list(self, request):
#         return Response("GET API")

#     def create(self, request):
#         file_uploaded = request.FILES.get('image')
#         content_type = file_uploaded.content_type
#         response = "POST API and you have uploaded a {} file".format(content_type)
#         return Response(response)



class ListBlogsAPI(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = BlogSerializer

    def get_queryset(self):
        blogs = Blogs.objects.all()
        return blogs


class DetailBlogAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = BlogSerializer

    def get_queryset(self, **kwargs):
        blog_id = self.kwargs["pk"]
        blog = Blogs.objects.all()
       # blog = get_object_or_404(Blogs, pk=blog_id)
        return blog

class UpdateBlogAPI(generics.UpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = BlogSerializer

    def partial_update(self, request, **kwargs):
        blog_id = self.kwargs["pk"]
        blog = get_object_or_404(Blogs, pk=blog_id, user=request.user)
        blog.title = request.data['title']
        blog.content = request.data['content']
        blog.save()

        return Response({
            'message': 'blog data is updated',
            'updated-blog': self.get_serializer(blog).data
        })

class BlogSearchAPI(generics.ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blogs.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

class DeleteBlogAPI(generics.RetrieveDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = BlogSerializer
    #queryset = Blogs.objects.all()

    def get_object(self, **kwargs):
        blog_id = self.kwargs['pk']
        queryset = get_object_or_404(Blogs, user=self.request.user, pk=blog_id)
        return queryset

    # def get_queryset(self, **kwargs):
    #     blog_id = self.kwargs["pk"]
    #     queryset = get_object_or_404(Blogs, user=self.request.user, pk=blog_id)
    #     return queryset

    # def perform_destroy(self):
    #     instance = self.get_queryset()
    #     instance.delete()
    #     return Response({
    #         'message':'blog is deleted'
    #     })


""" Concrete View Classes
# CreateAPIView
Used for create-only endpoints.
# ListAPIView
Used for read-only endpoints to represent a collection of model instances.
# RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
# DestroyAPIView
Used for delete-only endpoints for a single model instance.
# UpdateAPIView
Used for update-only endpoints for a single model instance.
# ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
# RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
# RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""