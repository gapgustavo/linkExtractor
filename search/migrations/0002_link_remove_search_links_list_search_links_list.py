# Generated by Django 4.2.3 on 2023-07-11 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='search',
            name='links_list',
        ),
        migrations.AddField(
            model_name='search',
            name='links_list',
            field=models.ManyToManyField(to='search.link'),
        ),
    ]
