# Generated by Django 4.1.7 on 2023-07-03 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agence', '0001_initial'),
        ('employee', '0005_employees_sexe'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='agence',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='agence.agence'),
        ),
    ]
