# Generated by Django 2.2.2 on 2019-06-18 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190512_2149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-Date',)},
        ),
    ]
