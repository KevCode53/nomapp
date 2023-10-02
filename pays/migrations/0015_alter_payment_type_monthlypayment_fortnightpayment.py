# Generated by Django 4.2.5 on 2023-10-02 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employees', '0015_alter_employee_gender_alter_familymember_gender_and_more'),
        ('pays', '0014_alter_payment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='type',
            field=models.CharField(choices=[('4', 'Aguinaldo'), ('1', 'Quincena'), ('3', 'Bono 14'), ('2', 'Mes')], default=1, max_length=15),
        ),
        migrations.CreateModel(
            name='MonthlyPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateField(auto_now=True, null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('credit_store', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('month', models.PositiveSmallIntegerField()),
                ('year', models.PositiveSmallIntegerField()),
                ('comision', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('social_security', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('contribution', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('credit', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'FortnightPayment',
                'verbose_name_plural': 'FortnightPayments',
            },
        ),
        migrations.CreateModel(
            name='FortnightPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateField(auto_now=True, null=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('credit_store', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('month', models.PositiveSmallIntegerField()),
                ('year', models.PositiveSmallIntegerField()),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'FortnightPayment',
                'verbose_name_plural': 'FortnightPayments',
            },
        ),
    ]