# Generated by Django 4.1 on 2023-05-30 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Categorie',
            },
        ),
        migrations.CreateModel(
            name='Prodotto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descrizione', models.TextField(blank=True, null=True)),
                ('prezzo', models.DecimalField(decimal_places=2, max_digits=7)),
                ('immagine', models.ImageField(blank=True, null=True, upload_to='')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prodotti.categoria')),
            ],
            options={
                'verbose_name_plural': 'Prodotti',
            },
        ),
    ]