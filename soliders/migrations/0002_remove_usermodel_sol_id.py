# Generated by Django 4.1.4 on 2022-12-28 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soliders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='sol_id',
        ),
    ]