# Generated by Django 5.0.3 on 2024-06-02 19:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Userapp", "0005_myrefaral"),
    ]

    operations = [
        migrations.AddField(
            model_name="myrefaral",
            name="date_referred",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
