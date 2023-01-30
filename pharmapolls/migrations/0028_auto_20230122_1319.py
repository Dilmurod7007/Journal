# Generated by Django 3.2 on 2023-01-22 08:19

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmapolls', '0027_auto_20230122_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_uz',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_en',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_uz',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
