# Generated by Django 4.1.2 on 2022-10-19 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Notes", "0004_remove_notescontroller_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="notescontroller",
            name="succes",
            field=models.BooleanField(default=False),
        ),
    ]
