# Generated by Django 3.1.1 on 2023-01-05 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soliders', '0002_remove_usermodel_sol_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soliders',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
