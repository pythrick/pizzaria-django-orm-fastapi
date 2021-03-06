# Generated by Django 3.2 on 2021-04-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sabor', models.CharField(max_length=100)),
                ('tamanho', models.CharField(choices=[('PEQUENA', 'Pequena'), ('MEDIA', 'Média'), ('GRANDE', 'Grande'), ('GIGANTE', 'Gigante')], max_length=10)),
            ],
            options={
                'verbose_name': 'Pizza',
                'verbose_name_plural': 'Pizzas',
                'db_table': 'pizzas',
            },
        ),
    ]
