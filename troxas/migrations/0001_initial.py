# Generated by Django 2.0.5 on 2018-05-13 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Troxa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=20)),
                ('sobrenome', models.CharField(max_length=30)),
                ('idade', models.IntegerField()),
            ],
        ),
    ]
