# Generated by Django 4.2.2 on 2023-06-19 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_blog_comment_comment_blog_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=221, null=True),
        ),
    ]
