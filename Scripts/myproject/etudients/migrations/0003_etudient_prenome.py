# Generated by Django 4.2 on 2023-05-10 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudients', '0002_remove_etudient_email_remove_etudient_prenome_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudient',
            name='prenome',
            field=models.CharField(default='null', max_length=30),
        ),
    ]
