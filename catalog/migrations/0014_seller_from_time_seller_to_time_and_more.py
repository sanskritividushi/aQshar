# Generated by Django 4.2.11 on 2024-03-30 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0013_donator_image_seller_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="seller",
            name="from_time",
            field=models.TimeField(default=9),
        ),
        migrations.AddField(
            model_name="seller",
            name="to_time",
            field=models.TimeField(default=22),
        ),
        migrations.AlterField(
            model_name="donator",
            name="from_time",
            field=models.TimeField(default=9),
        ),
    ]
