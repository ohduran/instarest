# Generated by Django 2.1.7 on 2019-03-07 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('password', models.CharField(max_length=50)),
                ('is_verified', models.BooleanField(default=False)),
                ('last_verified', models.DateTimeField(blank=True, null=True)),
                ('username', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
