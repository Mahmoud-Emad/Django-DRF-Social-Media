# Generated by Django 3.2.9 on 2021-12-14 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jornal_app', '0004_auto_20211214_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpage',
            name='posts',
            field=models.ManyToManyField(related_name='page_posts', to='jornal_app.Post'),
        ),
    ]
