# Generated by Django 4.1.5 on 2023-02-13 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmapolls', '0006_video_organization_en_video_organization_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video_gallery',
            name='title_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='video_gallery',
            name='title_ru',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='video_gallery',
            name='title_uz',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
