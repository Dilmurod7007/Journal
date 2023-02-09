# Generated by Django 4.1.5 on 2023-02-09 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pharmapolls", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="organization",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="pharmapolls.organization",
            ),
        ),
    ]