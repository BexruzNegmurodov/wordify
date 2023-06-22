from django.urls import path
from .views import blogs, detail, url_in_detail_page

app_name = 'blogs'

urlpatterns = [
    path('blog-list/', blogs, name='blog-list'),
    path('url_in_detail_page/<int:day>/<int:month>/<int:year>/<slug:slug>/', url_in_detail_page,
         name='url_in_detail_page'),
    path('detail/<int:day>/<int:month>/<int:year>/<slug:slug>/', detail, name='detail'),
]
