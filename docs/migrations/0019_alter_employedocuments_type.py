# Generated by Django 4.2.5 on 2023-10-03 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0018_alter_employedocuments_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employedocuments',
            name='type',
            field=models.CharField(choices=[('Identification', 1), ('Diplomas', 7), ('Antecedentes Policiacos', 3), ('Certificaciones', 6), ('Antecedentes Penales', 4), ('Titulos', 5), ('Curriculum', 2)], max_length=50),
        ),
    ]
