# Generated by Django 4.0.1 on 2022-02-21 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jornal_app', '0021_usersettings_language_usersettings_look_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersettings',
            name='language',
            field=models.JSONField(default={'code': 'en', 'country': 'us'}),
        ),
    ]