# Generated by Django 3.0.8 on 2020-09-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=300)),
                ('message', models.CharField(max_length=300)),
            ],
        ),
    ]
