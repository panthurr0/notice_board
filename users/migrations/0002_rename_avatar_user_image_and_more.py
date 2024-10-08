# Generated by Django 5.1 on 2024-08-11 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="avatar",
            new_name="image",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="phone_number",
            new_name="phone",
        ),
        migrations.RemoveField(
            model_name="user",
            name="city",
        ),
        migrations.RemoveField(
            model_name="user",
            name="tg_id",
        ),
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("user", "User"), ("admin", "Admin")],
                default="user",
                max_length=10,
                verbose_name="Роль",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=75, null=True, verbose_name="Имя пользователя"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                blank=True,
                max_length=75,
                null=True,
                verbose_name="Фамилия пользователя",
            ),
        ),
    ]
