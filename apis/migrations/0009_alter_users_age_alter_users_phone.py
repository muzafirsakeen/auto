# Generated by Django 4.1.2 on 2022-11-21 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apis", "0008_alter_driver_detail_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users", name="age", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="users", name="phone", field=models.BigIntegerField(),
        ),
    ]