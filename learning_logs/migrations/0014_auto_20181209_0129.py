# Generated by Django 2.1.3 on 2018-12-09 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0013_auto_20181209_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='text',
            field=models.TextField(),
        ),
    ]