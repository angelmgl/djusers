# Generated by Django 4.1.1 on 2022-09-07 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="age",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="edad"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("1", "hombre"), ("2", "mujer")],
                max_length=1,
                null=True,
                verbose_name="género",
            ),
        ),
    ]
