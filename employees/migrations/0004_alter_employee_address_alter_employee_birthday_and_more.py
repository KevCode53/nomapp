# Generated by Django 4.2.5 on 2023-09-19 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_familymember_relation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='relation',
            field=models.CharField(choices=[('Father', 'father'), ('Wife', 'wife'), ('Daughter', 'daughter'), ('Son', 'son'), ('Brother', 'brother'), ('Mother', 'motherr'), ('Sister', 'sister'), ('Husband', 'husband')], max_length=10),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='historicalfamilymember',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='historicalfamilymember',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalfamilymember',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='historicalfamilymember',
            name='relation',
            field=models.CharField(choices=[('Father', 'father'), ('Wife', 'wife'), ('Daughter', 'daughter'), ('Son', 'son'), ('Brother', 'brother'), ('Mother', 'motherr'), ('Sister', 'sister'), ('Husband', 'husband')], max_length=10),
        ),
    ]