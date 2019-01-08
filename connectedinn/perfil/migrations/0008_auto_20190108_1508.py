# Generated by Django 2.1.4 on 2019-01-08 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0007_perfil_bloqueado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloqueio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='bloqueado',
        ),
        migrations.AddField(
            model_name='bloqueio',
            name='perfil_bloqueado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bloqueado', to='perfil.Perfil'),
        ),
        migrations.AddField(
            model_name='bloqueio',
            name='perfil_bloqueador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bloqueador', to='perfil.Perfil'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='contatos_bloqueados',
            field=models.ManyToManyField(related_name='meus_contatos_bloqueados', through='perfil.Bloqueio', to='perfil.Perfil'),
        ),
    ]
