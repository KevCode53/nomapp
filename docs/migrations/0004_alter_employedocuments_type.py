# Generated by Django 4.2.5 on 2023-09-26 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0003_alter_employedocuments_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employedocuments',
            name='type',
            field=models.CharField(choices=[('Diplomas', 7), ('Identification', 1), ('Certificaciones', 6), ('Antecedentes Penales', 4), ('Curriculum', 2), ('Antecedentes Policiacos', 3), ('Titulos', 5)], max_length=50),
        ),
    ]