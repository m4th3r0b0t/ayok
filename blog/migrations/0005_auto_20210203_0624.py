# Generated by Django 3.1.5 on 2021-02-03 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_stats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_stats',
            name='vote',
            field=models.BooleanField(),
        ),
    ]
