# Generated by Django 3.1.5 on 2021-02-04 06:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_remove_vote_table_time_posted'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='comment_table',
            name='pk_comment',
        ),
        migrations.AlterUniqueTogether(
            name='comment_table',
            unique_together={('post', 'author')},
        ),
    ]
