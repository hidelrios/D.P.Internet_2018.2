# Generated by Django 2.1.3 on 2018-11-20 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(),
        ),
    ]
