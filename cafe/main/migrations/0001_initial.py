# Generated by Django 5.0.6 on 2024-06-28 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coffeeName', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('availability', models.BooleanField(default=True)),
                ('totalCount', models.IntegerField()),
                ('coffeeImage', models.ImageField(upload_to='coffeeImages/')),
            ],
            options={
                'db_table': 'coffee',
            },
        ),
    ]
