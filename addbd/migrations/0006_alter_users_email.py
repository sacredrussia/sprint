# Generated by Django 4.2.10 on 2024-02-28 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addbd', '0005_alter_passes_coordinates_alter_users_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=10000, unique=True),
        ),
    ]
