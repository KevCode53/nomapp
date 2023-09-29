# Generated by Django 4.2.5 on 2023-09-28 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0009_alter_employee_gender_alter_familymember_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='relation',
            field=models.CharField(choices=[('Husband', 'husband'), ('Sister', 'sister'), ('Father', 'father'), ('Mother', 'motherr'), ('Son', 'son'), ('Brother', 'brother'), ('Daughter', 'daughter'), ('Wife', 'wife')], max_length=10),
        ),
    ]
