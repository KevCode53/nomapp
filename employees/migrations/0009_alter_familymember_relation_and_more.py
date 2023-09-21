# Generated by Django 4.2.5 on 2023-09-21 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_alter_employee_gender_alter_familymember_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymember',
            name='relation',
            field=models.CharField(choices=[('Father', 'father'), ('Husband', 'husband'), ('Wife', 'wife'), ('Daughter', 'daughter'), ('Son', 'son'), ('Brother', 'brother'), ('Mother', 'motherr'), ('Sister', 'sister')], max_length=10),
        ),
        migrations.AlterField(
            model_name='historicalfamilymember',
            name='relation',
            field=models.CharField(choices=[('Father', 'father'), ('Husband', 'husband'), ('Wife', 'wife'), ('Daughter', 'daughter'), ('Son', 'son'), ('Brother', 'brother'), ('Mother', 'motherr'), ('Sister', 'sister')], max_length=10),
        ),
    ]