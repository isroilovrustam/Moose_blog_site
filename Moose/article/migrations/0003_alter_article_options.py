# Generated by Django 4.1.4 on 2022-12-19 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-id']},
        ),
    ]
