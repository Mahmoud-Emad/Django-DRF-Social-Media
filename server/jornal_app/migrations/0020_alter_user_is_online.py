# Generated by Django 4.0 on 2021-12-28 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jornal_app', '0019_user_is_online'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
    ]
