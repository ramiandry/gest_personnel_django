# Generated by Django 4.1.7 on 2023-03-29 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0002_remove_employees_mission"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employees",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="products/"),
        ),
    ]
