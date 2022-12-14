# Generated by Django 4.1.2 on 2022-11-10 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="pic1",
            field=models.ImageField(
                blank=True, default="", null=True, upload_to="uploads"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="pic2",
            field=models.ImageField(
                blank=True, default="", null=True, upload_to="uploads"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="pic3",
            field=models.ImageField(
                blank=True, default="", null=True, upload_to="uploads"
            ),
        ),
        migrations.CreateModel(
            name="Wishlist",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainApp.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mainApp.buyer"
                    ),
                ),
            ],
        ),
    ]
