# Generated by Django 2.0.1 on 2020-02-25 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='source',
            options={'managed': False, 'ordering': ['-create_time']},
        ),
    ]
