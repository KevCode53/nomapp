# Generated by Django 4.2.5 on 2023-10-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pays', '0032_alter_fortnightpayment_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='type',
            field=models.CharField(choices=[('3', 'Bono 14'), ('1', 'Quincena'), ('4', 'Aguinaldo'), ('2', 'Mes')], default=1, max_length=15),
        ),
    ]