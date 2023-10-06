# Generated by Django 4.2.5 on 2023-10-05 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pays', '0030_alter_payment_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fortnightpayment',
            name='month',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='fortnightpayment',
            name='year',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='monthlypayment',
            name='month',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='monthlypayment',
            name='year',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='type',
            field=models.CharField(choices=[('1', 'Quincena'), ('2', 'Mes'), ('3', 'Bono 14'), ('4', 'Aguinaldo')], default=1, max_length=15),
        ),
    ]