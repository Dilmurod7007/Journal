# Generated by Django 3.2 on 2023-01-20 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmapolls', '0020_auto_20230120_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='number_table',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]