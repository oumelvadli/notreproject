# Generated by Django 4.2 on 2023-05-10 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departements',
            fields=[
                ('id_depart', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nom_dep', models.CharField(max_length=255)),
                ('code_dep', models.CharField(max_length=10)),
            ],
        ),
    ]
