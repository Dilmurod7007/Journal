# Generated by Django 4.1.5 on 2023-02-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmapolls', '0045_user_groups_user_is_superuser_user_user_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurnal',
            name='archive',
            field=models.BooleanField(default=False),
        ),
    ]
