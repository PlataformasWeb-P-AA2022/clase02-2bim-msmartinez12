# Generated by Django 4.0.5 on 2022-06-13 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mundial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='nombre',
            field=models.CharField(default='hola', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='siglas',
            field=models.CharField(default='hola', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='sobrenombre',
            field=models.CharField(default='hola', max_length=30),
            preserve_default=False,
        ),
    ]
