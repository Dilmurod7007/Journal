# Generated by Django 4.1.5 on 2023-02-16 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmapolls', '0014_alter_subdivision_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdivision',
            name='position',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
