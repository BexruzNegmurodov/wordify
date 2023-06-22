from django.shortcuts import render
from blog.models import Category, Tags, Blog
from django.core.paginator import Paginator
from profiles.models import Profile


def home(request):
    obj = Blog.objects.order_by('-id')
    lates = Blog.objects.order_by('-id')[:3]
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
        'lates': lates,
    }
    return render(request, 'main/index.html', ctx)
