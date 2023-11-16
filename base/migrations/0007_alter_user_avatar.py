# Generated by Django 4.2.7 on 2023-11-16 10:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0006_alter_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                default="static/base/images/avatar.svg",
                null=True,
                upload_to="static/base/images/",
            ),
        ),
    ]
