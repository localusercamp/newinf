# Generated by Django 2.2.6 on 2019-11-17 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonus', '0009_auto_20191117_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonustransaction',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
