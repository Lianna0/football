# Generated by Django 4.2.6 on 2023-10-19 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_club'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='stadium_image',
            field=models.ImageField(upload_to='media/', verbose_name='Stadium Image'),
        ),
    ]
