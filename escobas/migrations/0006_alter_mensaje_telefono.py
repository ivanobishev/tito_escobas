# Generated by Django 3.2.3 on 2021-05-25 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escobas', '0005_rename_archivada_mensaje_archivado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
