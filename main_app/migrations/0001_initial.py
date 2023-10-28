# Generated by Django 4.2.6 on 2023-10-28 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('wingspan', models.FloatField()),
                ('lifespan', models.IntegerField()),
                ('is_migratory', models.BooleanField(default=False)),
            ],
        ),
    ]
