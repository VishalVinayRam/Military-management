# Generated by Django 4.1.4 on 2022-12-27 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('missions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Terrorist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('Mission_captured', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='missions.mission')),
            ],
        ),
    ]
