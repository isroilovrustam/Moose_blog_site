# Generated by Django 4.1.4 on 2022-12-19 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=303)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=303)),
                ('linkt', models.CharField(max_length=202)),
                ('linkf', models.CharField(max_length=202)),
                ('linki', models.CharField(max_length=204)),
            ],
        ),
    ]
