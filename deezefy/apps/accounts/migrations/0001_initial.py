# Generated by Django 3.1.5 on 2021-01-10 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('birthday', models.DateField(verbose_name='Dia do nascimento')),
                ('age', models.IntegerField(blank=True, verbose_name='Idade')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Listener',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Numero de Telefone')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user', verbose_name='Usario')),
            ],
            options={
                'verbose_name': 'Ouvinte',
                'verbose_name_plural': 'Ouvintes',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(max_length=200, verbose_name='Nome artistico')),
                ('biography', models.TextField(verbose_name='Biografia')),
                ('formation_year', models.IntegerField(verbose_name='Ano de formação')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Artista',
                'verbose_name_plural': 'Artistas',
            },
        ),
    ]