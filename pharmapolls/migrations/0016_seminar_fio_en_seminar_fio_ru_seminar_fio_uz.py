# Generated by Django 4.1.5 on 2023-02-17 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmapolls', '0015_subdivision_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminar',
            name='fio_en',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='seminar',
            name='fio_ru',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='seminar',
            name='fio_uz',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
