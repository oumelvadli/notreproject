# Generated by Django 4.2 on 2023-04-21 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudient',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('prenome', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'tbletudient',
            },
        ),
    ]
