# Generated by Django 4.2.5 on 2023-09-21 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0017_alter_employedocuments_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employedocuments',
            name='type',
            field=models.CharField(choices=[('Certificaciones', 6), ('Curriculum', 2), ('Diplomas', 7), ('Antecedentes Policiacos', 3), ('Antecedentes Penales', 4), ('Titulos', 5), ('Identification', 1)], max_length=50),
        ),
    ]