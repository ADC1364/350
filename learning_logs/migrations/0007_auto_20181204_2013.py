# Generated by Django 2.1.3 on 2018-12-04 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0006_auto_20181204_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='progress_made',
        ),
        migrations.AddField(
            model_name='entry',
            name='progress_made',
            field=models.CharField(choices=[('incomplete', 'incomplete'), ('complete', 'complete'), ('inprogress', 'inprogress')], default='incomplete', max_length=20),
        ),
    ]
