# Generated by Django 4.2.11 on 2024-03-30 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0018_remove_donator_from_time_remove_donator_to_time_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="donator",
            name="from_time",
            field=models.TimeField(default="09:00"),
        ),
        migrations.AddField(
            model_name="donator",
            name="to_time",
            field=models.TimeField(default="22:00"),
        ),
        migrations.AddField(
            model_name="seller",
            name="from_time",
            field=models.TimeField(default="09:00"),
        ),
        migrations.AddField(
            model_name="seller",
            name="to_time",
            field=models.TimeField(default="22:00"),
        ),
    ]
