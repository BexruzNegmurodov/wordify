from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator

from profiles.models import Profile
from .forms import CommentForm
from .models import Blog, SubBlog, Category, Tags, Comment


def blogs(request):
    obj = Blog.objects.order_by('-id')
    q = request.GET.get('q')
    travel = request.GET.get('travel')
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    if q:
        obj = obj.filter(title__icontains=q)
    if travel:
        obj = obj.filter(travel__title__exact=travel)
    if cat:
        obj = obj.filter(category__title__exact=cat)
    if tag:
        obj = obj.filter(tags__title__exact=tag)
    paginator = Paginator(obj, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    try:
        profile = Profile.objects.get(user_id=request.user.id)
    except:
        profile = None

    ctx = {
        'obj': page_obj,
        'profile': profile,
    }
    return render(request, 'blogs/blogs.html', ctx)


def url_in_detail_page(request, **kwargs):
    slug = kwargs.get('slug')
    day = kwargs.get('day')
    month = kwargs.get('month')
    year = kwargs.get('year')
    obj = get_object_or_404(Blog, day__day=day, day__month=month, day__year=year, slug=slug)
    obj.views += 1
    obj.save()
    url = reverse('blogs:detail', kwargs={
        'day': obj.day.day,
        'month': obj.day.month,
        'year': obj.day.year,
        'slug': obj.slug
    })
    return redirect(url)


def detail(request, **kwargs):
    slug = kwargs.get('slug')
    day = kwargs.get('day')
    month = kwargs.get('month')
    year = kwargs.get('year')
    obj = get_object_or_404(Blog, day__day=day, day__month=month, day__year=year, slug=slug)
    comments_reply = Comment.objects.filter(reply_to_comment__isnull=True, blog_id=obj.id)
    reply_to_comment_id = request.GET.get('reply_to_comment')
    try:
        profile = Profile.objects.get(user_id=request.user.id)
    except:
        profile = None
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = obj
            comment.reply_to_comment_id = reply_to_comment_id
            if request.user.is_authenticated:
                comment.name = str(profile.full_name)
                comment.email = profile.email
                comment.number = profile.number
                comment.image = profile.image
            comment.save()
            return redirect('.')
    obj1 = Blog.objects.order_by('-id')
    try:
        profile = Profile.objects.get(user_id=request.user.id)
    except:
        profile = None
    obj1 = obj1.filter(author=obj.author)[:3]

    ctx = {
        'obj': obj,
        'obj1': obj1,
        'profile': profile,
        'form': form,
        'comments_reply': comments_reply
    }

    return render(request, 'blogs/blog-single.html', ctx)
