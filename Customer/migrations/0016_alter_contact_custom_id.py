# Generated by Django 4.2.3 on 2023-10-15 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0015_contact_custom_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='custom_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]