# Generated by Django 4.2.1 on 2023-05-31 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0010_alter_viewcount_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views_count',
            field=models.IntegerField(default=0),
        ),
    ]
