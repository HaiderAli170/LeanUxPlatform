# Generated by Django 4.2.3 on 2023-11-10 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evaluator', '0005_forwardeddata_assigned_evaluator'),
    ]

    operations = [
        migrations.AddField(
            model_name='forwardeddata',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
