import os

from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    head_image = models.ImageField(upload_to='teamangel/images/%Y/%m/%d', blank=True)  # 이미지 폴더 지정하기
    file_upload = models.FileField(upload_to='teamangel/files/%Y/%m/%d', blank=True)  # 포스트에 파일 올리기
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/teamangel/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]  # -1의미는 확장자 의미를함 EX) ~~.html txt py doc csv