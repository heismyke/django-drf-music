# Generated by Django 5.0.1 on 2024-01-25 21:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="artist",
            old_name="title",
            new_name="name",
        ),
    ]
