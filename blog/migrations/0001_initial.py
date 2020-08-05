# Generated by Django 3.0.8 on 2020-08-05 08:39

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
                ('slug', models.SlugField(max_length=45, unique=True, verbose_name='Url')),
                ('description', models.TextField(max_length=300, verbose_name='Описание')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.Category')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(max_length=55, unique=True, verbose_name='Url')),
                ('pre_description', models.CharField(blank=True, max_length=40, null=True, verbose_name='Пред показ')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products', verbose_name='Изображение')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('to_display', models.BooleanField(default=False, verbose_name='Показать?')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('for_auth', models.BooleanField(default=False, verbose_name='Для авторизованных пользователей?')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='author.Author')),
                ('tag', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['created_date'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(max_length=55, unique=True, verbose_name='Url')),
                ('description', models.TextField(max_length=150, verbose_name='Описание')),
                ('text', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(blank=True, upload_to='posts', verbose_name='Изображение')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('to_display', models.BooleanField(default=False, verbose_name='Показать?')),
                ('for_auth', models.BooleanField(default=False, verbose_name='Для авторизованных пользователей?')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='author.Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='blog.Category')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='blog.Product')),
                ('tag', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['created_date'],
            },
        ),
    ]
