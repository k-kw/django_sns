# Generated by Django 3.2.5 on 2022-06-23 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0002_rename_user_postmsg_userprf'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmsg',
            name='imgflg',
            field=models.BooleanField(default=True),
        ),
    ]
