# Generated by Django 4.2 on 2023-05-10 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encadrents',
            fields=[
                ('id_encad', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nom_encad', models.CharField(max_length=30)),
                ('prenom_encad', models.CharField(max_length=30)),
                ('email_encad', models.CharField(max_length=30)),
            ],
        ),
    ]