# Generated by Django 5.0.1 on 2024-02-07 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
