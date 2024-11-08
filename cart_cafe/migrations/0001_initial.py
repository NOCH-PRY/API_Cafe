# Generated by Django 5.0.9 on 2024-10-04 17:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('added_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'cafe_cart',
            },
        ),
    ]
