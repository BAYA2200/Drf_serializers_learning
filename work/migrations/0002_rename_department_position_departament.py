# Generated by Django 3.2 on 2023-12-18 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='department',
            new_name='departament',
        ),
    ]