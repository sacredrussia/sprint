# Generated by Django 4.2.10 on 2024-03-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addbd', '0007_rename_beautytitle_passes_beauty_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passes',
            name='connect',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='passes',
            name='level_autumn',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='passes',
            name='level_spring',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='passes',
            name='level_summer',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='passes',
            name='level_winter',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='passes',
            name='other_titles',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]
