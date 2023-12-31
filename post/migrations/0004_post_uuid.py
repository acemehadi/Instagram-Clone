# Generated by Django 4.2.5 on 2023-10-26 05:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_remove_post_comments_remove_post_likes_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]