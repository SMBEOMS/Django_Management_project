from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CommentForm

from .models import Post, Category, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView


class PostList(ListView):
    model = Post
    ordering = '-pk' #ListView로 포스트 목록 페이지 만들기
    paginate_by = 4
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()  # post_list
        context['categories'] = Category.objects.all()
        context['comment_form'] = CommentForm
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['posts_by_views'] = Post.objects.all().order_by('-views')[:4]  # 조회수가 높은 게시글 5개
        return context  # -> post_list.html

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    # 페이지네이션 설정
    paginator = Paginator(post_list, 4)  # 페이지당 4개의 포스트 표시
    page = request.GET.get('page')
    post_list = paginator.get_page(page)

    is_paginated = post_list.has_other_pages()

    return render(
        request,
        'teamangel/category.html',
        {
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category,
            'post_list': post_list,
            'is_paginated': is_paginated,  # 추가
            'page_obj': post_list,  # 추가
            'paginator': paginator,
        }
    )



class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        return context

    def get_object(self):
        obj = super().get_object()
        obj.views += 1  # 조회수 증가
        obj.save()
        return obj


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'category', 'head_image', 'file_upload']
    template_name = 'teamangel/post_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context



class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'category', 'head_image', 'file_upload']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super(PostCreate, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def new_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)

        if request.method == "POST":
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
            else:
                return redirect(post.get_absolute_url())
        else:
            raise PermissionDenied

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    # comment_form.html

    def dispath(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(CommentUpdate, self).dispath(request, *args, **kwargs)
        else:
            raise PermissionDenied
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied

