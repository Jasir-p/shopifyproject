# Generated by Django 5.0.3 on 2024-05-02 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Order", "0007_order_address"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="trackig_id",
            new_name="order_id",
        ),
        migrations.AddField(
            model_name="orderproduct",
            name="trackig_id",
            field=models.CharField(default=None, max_length=20, null=True, unique=True),
        ),
    ]
