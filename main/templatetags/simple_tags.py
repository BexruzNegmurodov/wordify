from django import template
from profiles.models import Profile
from django.contrib.auth.models import User
from blog.models import Category, Tags, Travel, Blog

register = template.Library()


# @register.simple_tag()
# def user_profile():
#     profile = Profile.objects.get(user__username=User.username)
#     print(profile.full_name)
#     return profile


@register.simple_tag()
def category_my():
    obj = Category.objects.all()
    return obj


@register.simple_tag()
def tags_my():
    obj = Tags.objects.all()
    return obj


@register.simple_tag()
def travel_my():
    obj = Travel.objects.all()
    return obj


@register.simple_tag()
def latest_blogs():
    obj = Blog.objects.order_by('-id')[:3]
    return obj


@register.simple_tag()
def popular_blogs():
    return Blog.objects.order_by('-views')[:2]
