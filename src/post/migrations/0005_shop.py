# Generated by Django 2.2.3 on 2019-07-25 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20190724_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=10)),
                ('seats', models.CharField(max_length=10)),
                ('doors', models.CharField(max_length=10)),
                ('petrol', models.CharField(max_length=10)),
                ('ac', models.BooleanField(default=True)),
                ('gridbox', models.CharField(max_length=10)),
            ],
        ),
    ]