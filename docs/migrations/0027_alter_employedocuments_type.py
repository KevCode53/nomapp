# Generated by Django 4.2.5 on 2023-10-05 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0026_alter_employedocuments_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employedocuments',
            name='type',
            field=models.CharField(choices=[('Curriculum', 2), ('Antecedentes Penales', 4), ('Certificaciones', 6), ('Antecedentes Policiacos', 3), ('Identification', 1), ('Diplomas', 7), ('Titulos', 5)], max_length=50),
        ),
    ]
