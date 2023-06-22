from django.contrib import admin
import nested_admin
from .models import Tags, Category, Blog, SubBlog, ImageSubBlog, Travel, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'name', 'parents_comment', 'reply_to_comment')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(ImageSubBlog)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'subblog')


@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class ImageInline(nested_admin.NestedTabularInline):
    model = ImageSubBlog
    extra = 0


class SubBlogInline(nested_admin.NestedTabularInline):
    model = SubBlog
    inlines = [ImageInline]
    extra = 0


class BlogAdmin(nested_admin.NestedModelAdmin):
    inlines = [SubBlogInline]
    list_display = ('id', 'author', 'title')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('author', 'title')
    filter_horizontal = ('tags',)


admin.site.register(Blog, BlogAdmin)
