# Generated by Django 4.0.1 on 2022-02-21 12:38

from django.db import migrations, models
import server.jornal_app.models.users


class Migration(migrations.Migration):

    dependencies = [
        ('jornal_app', '0022_alter_usersettings_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersettings',
            name='language',
            field=models.JSONField(default=server.jornal_app.models.users.default_language),
        ),
    ]