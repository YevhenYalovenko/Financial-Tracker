# Generated by Django 4.2.5 on 2023-10-03 14:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="wallet",
            name="balance_in_uah",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]
