# Generated by Django 4.2.5 on 2023-09-21 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pays', '0004_alter_prepaid_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='prepaid',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='prepaid',
            constraint=models.UniqueConstraint(fields=('employee', 'year', 'month'), name='prepay_unique_contrain'),
        ),
    ]
