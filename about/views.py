from django.shortcuts import render
from blog.models import Blog
from profiles.models import Profile
from django.core.paginator import Paginator


def about(request):
    obj = Blog.objects.order_by('-id')
    try:
        profile = Profile.objects.get(user_id=request.user.id)
    except:
        profile = None

    obj = obj.filter(author=profile)
    paginator = Paginator(obj, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    ctx = {
        'obj': page_obj,
        'profile': profile
    }
    return render(request, 'about/about.html', ctx)
