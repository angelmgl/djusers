# Generated by Django 4.1.1 on 2022-09-09 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_age_alter_user_gender"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False, verbose_name="staff"),
        ),
    ]
