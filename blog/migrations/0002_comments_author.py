# Generated by Django 2.2.1 on 2019-06-15 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.CharField(default='user', max_length=20),
        ),
    ]
