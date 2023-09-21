# Generated by Django 4.2.5 on 2023-09-21 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pays', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prepaid',
            name='month',
            field=models.PositiveSmallIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prepaid',
            name='year',
            field=models.PositiveSmallIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
    ]