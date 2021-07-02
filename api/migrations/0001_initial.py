# Generated by Django 3.2.5 on 2021-07-02 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EntryPoint",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("refresh_time", models.DateTimeField()),
                ("bid_price", models.DecimalField(decimal_places=2, max_digits=15)),
                ("ask_price", models.DecimalField(decimal_places=2, max_digits=15)),
                ("exchange_rate", models.DecimalField(decimal_places=2, max_digits=15)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
