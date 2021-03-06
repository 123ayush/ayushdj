# Generated by Django 3.1.7 on 2021-02-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalis', models.TextField()),
                ('title', models.CharField(max_length=150, unique=True)),
                ('created_at', models.DateField()),
                ('slug', models.CharField(max_length=150, unique=True)),
                ('status', models.BooleanField(default=0)),
                ('image', models.ImageField(upload_to='slider')),
            ],
        ),
    ]
