# Generated by Django 2.2 on 2021-07-13 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration_app', '0003_auto_20210713_0602'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(null='TRUE'),
            preserve_default='TRUE',
        ),
    ]