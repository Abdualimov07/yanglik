# Generated by Django 4.1.7 on 2023-05-02 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0004_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='media/yangiliklar.uz/image/image'),
        ),
    ]
