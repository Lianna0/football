# Generated by Django 4.2.6 on 2023-10-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('country', models.CharField(max_length=40)),
                ('club', models.CharField(max_length=50)),
                ('age', models.PositiveSmallIntegerField(default=20)),
            ],
            options={
                'verbose_name': 'Players',
                'verbose_name_plural': 'Players',
            },
        ),
    ]