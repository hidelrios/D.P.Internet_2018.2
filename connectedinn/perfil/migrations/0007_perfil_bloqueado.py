# Generated by Django 2.1.4 on 2019-01-08 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0006_auto_20190108_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='bloqueado',
            field=models.ManyToManyField(related_name='_perfil_bloqueado_+', to='perfil.Perfil'),
        ),
    ]