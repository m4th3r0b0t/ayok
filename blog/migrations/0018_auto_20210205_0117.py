# Generated by Django 3.1.5 on 2021-02-04 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20210205_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='time_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
