# Generated by Django 2.1.3 on 2018-12-09 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0014_auto_20181209_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='status',
            field=models.TextField(choices=[('complete', 'complete'), ('incomplete', 'incomplete')], default='incomplete', max_length=10),
        ),
        migrations.AlterField(
            model_name='topic',
            name='priority',
            field=models.TextField(choices=[('high', 'high'), ('medium', 'medium'), ('low', 'low')], default='medium', max_length=6),
        ),
    ]