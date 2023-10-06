# Generated by Django 4.2.5 on 2023-10-06 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pays', '0031_alter_fortnightpayment_month_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fortnightpayment',
            options={'ordering': ['year', 'month'], 'verbose_name': 'FortnightPayment', 'verbose_name_plural': 'FortnightPayments'},
        ),
        migrations.AlterModelOptions(
            name='monthlypayment',
            options={'ordering': ['year', 'month'], 'verbose_name': 'MonthlyPayment', 'verbose_name_plural': 'MonthlyPayments'},
        ),
        migrations.AddField(
            model_name='fortnightpayment',
            name='type_payment',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='monthlypayment',
            name='type_payment',
            field=models.PositiveSmallIntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='payment',
            name='type',
            field=models.CharField(choices=[('3', 'Bono 14'), ('2', 'Mes'), ('4', 'Aguinaldo'), ('1', 'Quincena')], default=1, max_length=15),
        ),
    ]