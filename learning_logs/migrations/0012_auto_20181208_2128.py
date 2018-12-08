# Generated by Django 2.1.3 on 2018-12-08 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0011_entry_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='status',
            field=models.CharField(choices=[('complete', 'complete'), ('incomplete', 'incomplete')], default='incomplete', max_length=10),
        ),
    ]
