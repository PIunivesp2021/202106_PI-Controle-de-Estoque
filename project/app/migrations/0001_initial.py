# Generated by Django 3.2.8 on 2021-10-27 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Controle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empenho', models.IntegerField()),
                ('Nota_Fiscal', models.IntegerField()),
                ('Obs', models.CharField(max_length=150)),
                ('Material', models.CharField(max_length=100)),
            ],
        ),
    ]
