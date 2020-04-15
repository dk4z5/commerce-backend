# Generated by Django 3.0.2 on 2020-03-03 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('descricao', models.CharField(blank=True, max_length=120)),
                ('quantidade', models.IntegerField()),
                ('quantidade_alerta', models.IntegerField(verbose_name='Quantidade Mínima para alerta')),
                ('preco_base', models.FloatField(verbose_name='Preço da únidade')),
                ('data_insercao', models.DateTimeField(verbose_name='Data de inserção do produto no banco de dados.')),
                ('desconto', models.FloatField(verbose_name='Porcentagem de desconto')),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('valido', models.BooleanField()),
                ('data_validade', models.DateTimeField(verbose_name='Validade do produto.')),
                ('data_chegada', models.DateTimeField(verbose_name='Data de chegada.')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='estoque.Produto')),
            ],
        ),
    ]