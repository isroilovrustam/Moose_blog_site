# Generated by Django 4.1.4 on 2022-12-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=404)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=202)),
                ('about', models.CharField(max_length=303)),
            ],
        ),
    ]