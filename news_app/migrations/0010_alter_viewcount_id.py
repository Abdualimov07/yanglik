# Generated by Django 4.2.1 on 2023-05-31 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0009_viewcount_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewcount',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
