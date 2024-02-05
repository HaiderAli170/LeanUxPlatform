# Generated by Django 4.2.1 on 2023-12-19 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Evaluator', '0012_remove_eyetrackingdata_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emotionrecord',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='emotionrecord',
            name='emotion',
            field=models.CharField(max_length=20),
        ),
    ]
