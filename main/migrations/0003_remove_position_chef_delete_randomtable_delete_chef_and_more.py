# Generated by Django 4.2.5 on 2023-09-19 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_chef_randomtable_position_chef'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='chef',
        ),
        migrations.DeleteModel(
            name='RandomTable',
        ),
        migrations.DeleteModel(
            name='Chef',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]
