# Generated by Django 3.2.5 on 2022-09-23 10:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctime', models.DateTimeField(default=django.utils.timezone.now)),
                ('flwee_prf', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='followee', to='userprofile.userprofile')),
                ('flwer_prf', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='follower', to='userprofile.userprofile')),
            ],
        ),
    ]
