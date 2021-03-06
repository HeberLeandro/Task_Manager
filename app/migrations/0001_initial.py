# Generated by Django 2.2.19 on 2021-03-20 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('expiration_date', models.DateField()),
                ('priority', models.CharField(choices=[('H', 'High'), ('N', 'Normal'), ('L', 'Low')], max_length=1)),
            ],
        ),
    ]
