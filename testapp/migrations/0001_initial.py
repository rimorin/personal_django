# Generated by Django 3.1.2 on 2020-10-15 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('status', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(verbose_name='user created date')),
            ],
        ),
    ]
