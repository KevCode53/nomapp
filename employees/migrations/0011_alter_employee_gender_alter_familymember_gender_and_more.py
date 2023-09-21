# Generated by Django 4.2.5 on 2023-09-21 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0010_alter_familymember_relation_and_more'),
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
            field=models.CharField(choices=[('Sister', 'sister'), ('Brother', 'brother'), ('Mother', 'motherr'), ('Son', 'son'), ('Wife', 'wife'), ('Father', 'father'), ('Daughter', 'daughter'), ('Husband', 'husband')], max_length=10),
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
            field=models.CharField(choices=[('Sister', 'sister'), ('Brother', 'brother'), ('Mother', 'motherr'), ('Son', 'son'), ('Wife', 'wife'), ('Father', 'father'), ('Daughter', 'daughter'), ('Husband', 'husband')], max_length=10),
        ),
    ]