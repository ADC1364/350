# Generated by Django 2.1.3 on 2018-12-04 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_topic_progress_made'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='progress_made',
            field=models.CharField(choices=[('incomplete', 'incomplete'), ('complete', 'complete'), ('inprogress', 'inprogress')], default='incomplete', max_length=20),
        ),
    ]