# Generated by Django 4.2.4 on 2023-09-06 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_guide'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guide',
            old_name='desc',
            new_name='desc1',
        ),
        migrations.RenameField(
            model_name='guide',
            old_name='img',
            new_name='img1',
        ),
        migrations.RenameField(
            model_name='guide',
            old_name='name',
            new_name='name1',
        ),
    ]
