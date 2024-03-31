# Generated by Django 4.2.11 on 2024-03-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0012_remove_donator_image_remove_seller_from_time_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="donator",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="item_images"),
        ),
        migrations.AddField(
            model_name="seller",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="item_images"),
        ),
    ]
