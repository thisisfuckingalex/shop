# Generated by Django 3.0.8 on 2020-08-12 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100000, unique=True, verbose_name='id')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('to_display', models.BooleanField(default=False, verbose_name='Принята заявку или нет')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
    ]
