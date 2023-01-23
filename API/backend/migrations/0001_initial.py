# Generated by Django 4.1.5 on 2023-01-21 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type1', models.CharField(max_length=50)),
                ('type2', models.CharField(blank=True, max_length=50)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('img_1', models.CharField(max_length=100)),
                ('img_2', models.CharField(max_length=100)),
                ('img_3', models.CharField(max_length=100)),
                ('img_4', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Pokemon',
                'verbose_name_plural': 'Pokemones',
                'ordering': ['id'],
            },
        ),
    ]
