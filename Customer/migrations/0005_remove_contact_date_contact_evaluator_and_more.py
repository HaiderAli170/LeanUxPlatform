# Generated by Django 4.2.3 on 2023-10-12 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Evaluator', '0001_initial'),
        ('Customer', '0004_alter_contact_email_alter_contact_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
        migrations.AddField(
            model_name='contact',
            name='evaluator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Evaluator.evaluator'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='webName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
