# Generated by Django 3.2 on 2023-01-20 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmapolls', '0021_alter_organization_number_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurnal',
            name='author_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmapolls.author'),
        ),
        migrations.AddField(
            model_name='jurnal',
            name='author_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmapolls.author'),
        ),
        migrations.AddField(
            model_name='jurnal',
            name='author_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmapolls.author'),
        ),
        migrations.AddField(
            model_name='jurnal',
            name='organization_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmapolls.organization'),
        ),
        migrations.AddField(
            model_name='jurnal',
            name='organization_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmapolls.organization'),
        ),
        migrations.AddField(
            model_name='jurnal',
            name='organization_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmapolls.organization'),
        ),
    ]
