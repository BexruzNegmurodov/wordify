# Generated by Django 4.2.2 on 2023-06-22 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_comment_parents_comment_comment_reply_to_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='reply_to_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.comment'),
        ),
    ]
