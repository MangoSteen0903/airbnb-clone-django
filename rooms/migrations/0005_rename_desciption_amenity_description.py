# Generated by Django 4.1 on 2022-09-03 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0004_alter_amenity_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="amenity",
            old_name="desciption",
            new_name="description",
        ),
    ]
