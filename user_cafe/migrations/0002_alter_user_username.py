# Generated by Django 5.0.9 on 2024-10-09 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_cafe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]