# Generated by Django 4.1.2 on 2022-11-10 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0002_alter_product_pic1_alter_product_pic2_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="wishlist", old_name="name", new_name="Product",
        ),
    ]
