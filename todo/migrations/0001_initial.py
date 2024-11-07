# Generated by Django 5.1.3 on 2024-11-07 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('sub_title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('None', 'None'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default=('None', 'None'), max_length=50)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('is_done', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]