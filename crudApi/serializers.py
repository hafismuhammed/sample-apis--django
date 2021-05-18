from rest_framework import serializers
from .models import Blogs, UserImages


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blogs
        fields = '__all__'


class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = ('id', 'user', 'title', 'content')

    def create(self, validated_data):
        blog = Blogs.objects.create(
            user = self.context['request'].user,
            title = validated_data['title'],
            content = validated_data['content']
            )
        return blog

class UserImageSerializer(serializers.ModelSerializer):
    #image = serializers.ImageField(max_length=200)
    
    class Meta:
        model = UserImages
        fields = ('id', 'image', 'user')
    
    # def create(self, validated_data):
    #     return UserImages.objects.create(**validated_data)

    # def create(self, validated_data):
    #     image = UserImages.objects.create(
    #         user = self.context['request'].user,
    #         image = validated_data['image']
    #     )
    #     return image