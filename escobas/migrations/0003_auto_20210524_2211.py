# Generated by Django 3.2.3 on 2021-05-24 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escobas', '0002_auto_20210522_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='archivada',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]