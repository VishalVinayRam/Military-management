# Generated by Django 3.1.1 on 2023-01-15 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soliders', '0005_leave_letter_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave_letter_form',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
