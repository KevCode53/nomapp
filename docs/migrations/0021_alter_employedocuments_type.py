# Generated by Django 4.2.5 on 2023-10-04 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0020_alter_employedocuments_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employedocuments',
            name='type',
            field=models.CharField(choices=[('Titulos', 5), ('Identification', 1), ('Antecedentes Penales', 4), ('Antecedentes Policiacos', 3), ('Diplomas', 7), ('Certificaciones', 6), ('Curriculum', 2)], max_length=50),
        ),
    ]
