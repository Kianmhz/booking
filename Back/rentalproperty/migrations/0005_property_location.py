# Generated by Django 5.1.3 on 2024-11-27 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalproperty', '0004_alter_amenities_options_alter_property_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
    ]