# Generated by Django 5.0.6 on 2024-06-26 05:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_oredr_orderitem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Oredr',
            new_name='Order',
        ),
    ]
