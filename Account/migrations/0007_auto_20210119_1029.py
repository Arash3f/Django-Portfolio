# Generated by Django 3.1.4 on 2021-01-19 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_auto_20210118_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True, verbose_name='title')),
                ('about', models.TextField(blank=True, max_length=100, null=True, verbose_name='about')),
            ],
        ),
        migrations.AlterField(
            model_name='skill',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='name'),
        ),
    ]