# Generated by Django 4.2.11 on 2024-03-30 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0011_alter_donator_from_time_alter_donator_mobile_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="donator",
            name="image",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="from_time",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="image",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="to_time",
        ),
        migrations.DeleteModel(
            name="Cart",
        ),
    ]
