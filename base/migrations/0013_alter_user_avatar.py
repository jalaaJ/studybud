# Generated by Django 4.2.7 on 2023-11-16 10:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0012_alter_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                default="images/avatar.svg", null=True, upload_to=""
            ),
        ),
    ]
