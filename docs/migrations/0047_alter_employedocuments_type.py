# Generated by Django 4.2.5 on 2023-10-21 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0046_alter_employedocuments_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employedocuments',
            name='type',
            field=models.CharField(choices=[('Curriculum', 2), ('Certificaciones', 6), ('Identification', 1), ('Antecedentes Policiacos', 3), ('Diplomas', 7), ('Titulos', 5), ('Antecedentes Penales', 4)], max_length=50),
        ),
    ]
