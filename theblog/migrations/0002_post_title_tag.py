# Generated by Django 3.2.9 on 2021-11-12 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='WOW Blog!', max_length=255),
        ),
    ]