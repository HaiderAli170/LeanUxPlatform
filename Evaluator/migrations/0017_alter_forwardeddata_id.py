# Generated by Django 4.2.1 on 2024-01-20 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evaluator', '0016_emotiondata_project_alter_emotiondata_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forwardeddata',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]