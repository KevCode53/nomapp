# Generated by Django 4.2.5 on 2023-10-05 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pays', '0024_alter_payment_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monthlypayment',
            options={'verbose_name': 'MonthlyPayment', 'verbose_name_plural': 'MonthlyPayments'},
        ),
        migrations.AlterField(
            model_name='payment',
            name='type',
            field=models.CharField(choices=[('3', 'Bono 14'), ('4', 'Aguinaldo'), ('2', 'Mes'), ('1', 'Quincena')], default=1, max_length=15),
        ),
    ]