from django.db import models
from profiles.models import Profile
from django.shortcuts import reverse
from django.db.models.signals import post_save


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Tags(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Travel(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Blog(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    travel = models.OneToOneField(Travel, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='image')
    title = models.CharField(max_length=221)
    slug = models.SlugField(unique_for_date='created_date')
    text = models.TextField()
    created_date = models.TimeField(auto_now_add=True)
    modified_date = models.TimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tags)
    # comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    views = models.IntegerField(default=0)
    day = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.title}-->{self.id}'

    @property
    def full_url(self):
        url = reverse('blogs:url_in_detail_page', kwargs={
            'day': self.day.day,
            'month': self.day.month,
            'year': self.day.year,
            'slug': self.slug
        })
        return url


class Comment(models.Model):
    name = models.CharField(max_length=221, null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    parents_comment = models.IntegerField(blank=True, null=True)
    reply_to_comment = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='comment_image', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    number = models.IntegerField(null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def get_children(self):
        children = Comment.objects.filter(parents_comment=self.id).exclude(id=self.parents_comment)
        print(type(children))
        return children


def parents_post_save(instance, sender, created, *args, **kwargs):
    if created:
        parents = instance
        while parents.reply_to_comment:
            parents = parents.reply_to_comment
        instance.parents_comment = parents.id
        instance.save()
    return instance


post_save.connect(parents_post_save, sender=Comment)


class SubBlog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=221, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class ImageSubBlog(models.Model):
    subblog = models.ForeignKey(SubBlog, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='image', )
    is_wide = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
