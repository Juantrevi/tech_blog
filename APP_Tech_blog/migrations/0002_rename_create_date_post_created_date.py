# Generated by Django 4.2.1 on 2023-05-17 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP_Tech_blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_date',
            new_name='created_date',
        ),
    ]
