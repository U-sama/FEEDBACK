# Generated by Django 4.1.3 on 2022-12-21 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="image",
            field=models.FileField(upload_to="images"),
        ),
    ]
