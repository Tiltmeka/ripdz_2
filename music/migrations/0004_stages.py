# Generated by Django 3.1.4 on 2021-01-18 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20201220_0342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(max_length=50, verbose_name='Название площадки')),
                ('test', models.ManyToManyField(to='music.Band')),
            ],
        ),
    ]
