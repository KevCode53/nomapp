# Generated by Django 4.2.5 on 2023-09-21 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0014_alter_employee_gender_alter_familymember_gender_and_more'),
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
            field=models.CharField(choices=[('Wife', 'wife'), ('Husband', 'husband'), ('Sister', 'sister'), ('Mother', 'motherr'), ('Brother', 'brother'), ('Daughter', 'daughter'), ('Father', 'father'), ('Son', 'son')], max_length=10),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='historicalfamilymember',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='historicalfamilymember',
            name='relation',
            field=models.CharField(choices=[('Wife', 'wife'), ('Husband', 'husband'), ('Sister', 'sister'), ('Mother', 'motherr'), ('Brother', 'brother'), ('Daughter', 'daughter'), ('Father', 'father'), ('Son', 'son')], max_length=10),
        ),
    ]
