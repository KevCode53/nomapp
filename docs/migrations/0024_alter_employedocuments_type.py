# Generated by Django 4.2.5 on 2023-10-05 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0023_alter_employedocuments_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employedocuments',
            name='type',
            field=models.CharField(choices=[('Diplomas', 7), ('Antecedentes Penales', 4), ('Curriculum', 2), ('Titulos', 5), ('Antecedentes Policiacos', 3), ('Certificaciones', 6), ('Identification', 1)], max_length=50),
        ),
    ]