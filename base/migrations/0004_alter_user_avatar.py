# Generated by Django 4.2.7 on 2023-11-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0003_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(default="base/avatar.svg", null=True, upload_to=""),
        ),
    ]