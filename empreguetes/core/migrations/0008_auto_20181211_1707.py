# Generated by Django 2.1.3 on 2018-12-11 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20181210_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CategoriaCliente'),
        ),
    ]
