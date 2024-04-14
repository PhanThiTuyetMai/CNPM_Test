from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


class User(AbstractUser):
    avatar = CloudinaryField(default ='https://res.cloudinary.com/duz2xltvs/image/upload/v1711390925/unghi7vkrcec7tx1fhbr.jpg')


class BaseModel(models.Model):
    object = models.Manager()
    created_date = models.DateTimeField(auto_created=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Course(BaseModel):
    name = models.CharField(max_length=255)
    description = RichTextField()
    image = CloudinaryField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    subject = models.CharField(max_length=255, null=False)
    content = RichTextField()
    image = CloudinaryField()
    # on_delete=models.CASCADE là dùng cho khóa ngoại thì nếu xóa khóa học thì bài học sẽ mất lun
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', null=True, blank=True)

    def __str__(self):
        return self.subject


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Interaction(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Comment(Interaction):
    content = models.CharField(max_length=255)


class Like(Interaction):
    class Meta:
        unique_together = ('lesson', 'user')
