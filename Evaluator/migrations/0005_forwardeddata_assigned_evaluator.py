# Generated by Django 4.2.3 on 2023-11-10 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evaluator', '0004_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='forwardeddata',
            name='assigned_evaluator',
            field=models.CharField(max_length=100, null=True),
        ),
    ]