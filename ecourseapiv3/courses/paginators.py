from rest_framework import pagination


# Tạo phân trang cho course
class CoursePaginator(pagination.PageNumberPagination):
    page_size = 5
