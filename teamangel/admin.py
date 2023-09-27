from django.contrib import admin
from .models import Post, Category, Comment, PostImage  # PostImage 모델을 임포트합니다.

# PostImage 모델을 인라인으로 표시하기 위한 클래스를 정의합니다.
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

# Post 모델의 관리자 페이지 설정을 정의합니다.
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]

admin.site.register(Post, PostAdmin)  # Post 모델을 관리자 페이지에 등록하면서 설정을 적용합니다.
admin.site.register(Comment)
admin.site.register(PostImage)  # PostImage 모델을 관리자 페이지에 등록합니다.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
