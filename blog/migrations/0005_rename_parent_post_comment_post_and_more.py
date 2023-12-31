# Generated by Django 4.2.4 on 2023-08-13 10:18

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0004_remove_comment_is_edited_alter_comment_author_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="parent_post",
            new_name="post",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="comment_image",
        ),
        migrations.RemoveField(
            model_name="post",
            name="post_image",
        ),
        migrations.AddField(
            model_name="comment",
            name="image",
            field=models.ImageField(
                null=True, upload_to=blog.models.blog_image_file_path
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(
                null=True, upload_to=blog.models.blog_image_file_path
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
