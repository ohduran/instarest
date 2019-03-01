# Generated by Django 2.1.7 on 2019-03-01 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bots', '0005_bot_last_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bots.Bot')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]