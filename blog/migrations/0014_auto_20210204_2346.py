# Generated by Django 3.1.5 on 2021-02-04 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20210204_2313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='comment',
            new_name='content',
        ),
    ]
