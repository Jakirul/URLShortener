# Generated by Django 4.0.2 on 2022-02-02 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='shortened_url',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]