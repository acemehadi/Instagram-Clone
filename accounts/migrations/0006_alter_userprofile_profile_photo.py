# Generated by Django 4.2.5 on 2023-10-15 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userprofile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(default='profile/default.jpg', upload_to='profile'),
        ),
    ]
