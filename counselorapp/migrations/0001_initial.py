# Generated by Django 4.2.4 on 2024-06-03 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='uploaddetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myfile', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=30)),
                ('edu', models.CharField(max_length=100)),
                ('spec', models.CharField(max_length=400)),
                ('date', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=10)),
            ],
        ),
    ]
