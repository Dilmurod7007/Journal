# Generated by Django 3.2 on 2023-01-20 10:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmapolls', '0019_auto_20230120_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurnal',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='jurnal',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='jurnal',
            name='description_uz',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='jurnal',
            name='name_en',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='jurnal',
            name='name_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='jurnal',
            name='name_uz',
            field=models.CharField(max_length=500, null=True),
        ),
    ]