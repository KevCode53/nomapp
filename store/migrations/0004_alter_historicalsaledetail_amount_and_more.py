# Generated by Django 4.2.5 on 2023-09-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_historicalsale_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsaledetail',
            name='amount',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='saledetail',
            name='amount',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]