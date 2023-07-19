# 어플리케이션의 로직이 들어갑니다.각 뷰는 HTTP요청을 받아 처리하고 응답을 반환
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .forms import EmailPostForm
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class PostListView(ListView):
    # 대체글 목록뷰
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


# Create your views here.
def post_list(request):
    per_page = request.GET.get('per_page', 3)
    post_list = Post.published.all()
    # paginator = Paginator(post_list, 3) # 페이지당 3개의 게시물로 페이지네이션
    paginator = Paginator(post_list, per_page, orphans=1)
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # page_number가 정수가 아닌 경우 첫 번째 페이지 제공
        posts = paginator.page(1)
    except EmptyPage:
        # page_number가 범위를 벗어난 경우 결과의 마지막 페이지 제공
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    # 날짜 및 post인수를 받아와 주어진 슬러그와 출판일을 가진 게시글 검색
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})


def post_share(request, post_id):
    # id로 게시물 조회
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        # 폼이 제출되었을 때
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # 폼 필드가 유효성 검사를 통과
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']}님이 {post.title}을(를) 추천합니다."
            message = f"{post.title}을(를) 다음에서 읽어보세요.\n\n" \
                      f"{cd['name']}의 의견: {cd['comments']}"
            send_mail(subject, message, 'your_account@gmail.com', [cd['to']])
        sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent, })
