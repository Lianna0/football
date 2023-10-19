# Generated by Django 4.2.6 on 2023-10-19 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_player_options_player_foot_player_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('league', models.CharField(choices=[('Premier League', 'Premier League'), ('Bundesliga', 'Bundesliga'), ('La Liga', 'La Liga'), ('Serie A', 'Serie A'), ('Ligue 1', 'Ligue 1')], max_length=20)),
                ('stadium', models.CharField(max_length=100)),
                ('stadium_image', models.ImageField(upload_to='media/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Club',
                'verbose_name_plural': 'Clubs',
            },
        ),
    ]