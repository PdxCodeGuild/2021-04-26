# Generated by Django 3.2.4 on 2021-07-16 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_auto_20210716_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='types',
            field=models.ManyToManyField(related_name='pokemonmodel', to='pokedex.PokemonType'),
        ),
    ]