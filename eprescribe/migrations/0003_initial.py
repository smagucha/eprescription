# Generated by Django 4.1 on 2022-08-24 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eprescribe', '0002_delete_prescribemed'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrescribeMed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physcian', models.CharField(max_length=50)),
                ('entry_date', models.DateField(auto_now_add=True)),
                ('prescription', models.TextField()),
                ('patient_name', models.CharField(max_length=50)),
            ],
        ),
    ]
