from rest_framework import viewsets, generics, status, parsers
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Course, Lesson, User
from . import serializers, paginators


# chưa tạo ra API mà mình kế thừa để tạo API
class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.object.all()
    serializer_class = serializers.CategorySerializer


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.object.filter(active=True)
    serializer_class = serializers.CourseSerializer
    pagination_class = paginators.CoursePaginator

    def get_queryset(self):
        queryset = self.queryset

        q = self.request.query_params.get('q')
        if q:
            queryset = queryset.filter(name__icontains=q)

        cate_id = self.request.query_params.get('category_id')
        if cate_id:
            queryset = queryset.filter(category_id=cate_id)

        return queryset

    # gắn phương thức cho get/post cho API
    @action(methods=['get'], url_path='lessons', detail=True)
    def get_lessons(self, request, pk):
        # trả về cho mình cái đối tượng
        lessons = self.get_object().lesson_set.filter(active=True)  # lấy danh sách bài học
        return Response(serializers.LessonSerializer(lessons, many=True).data,
                        status=status.HTTP_200_OK)


class LessonViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    # lấy lun tag ra ngay lần truy vấn đầu tiên
    queryset = Lesson.object.prefetch_related('tags').filter(active=True)
    serializer_class = serializers.LessonSerializer


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.UserSerializer
    parser_classes = [parsers.MultiPartParser, ]

