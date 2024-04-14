from rest_framework import serializers
from .models import Category, Course, Lesson, Tag, User


# Tạo API cho category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# đè lại đường link để nó hiện ra đường link tuyệt đối của hình ảnh
class ItemSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        req = super().to_representation(instance)
        req['image'] = instance.image.url
        return req


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class CourseSerializer(ItemSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'image', 'created_date']


class LessonSerializer(ItemSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'image']


class LessonDetailSerializer(LessonSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = LessonSerializer.Meta.model
        fields = LessonSerializer.Meta.fields = ['content', 'tags']


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        data = validated_data.copy()
        # Cách 1: user = User(username=data['username', ])
        # Cách 2:
        user = User(**data)
        user.set_password(user.password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'avatar']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
