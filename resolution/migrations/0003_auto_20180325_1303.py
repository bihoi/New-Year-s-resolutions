# Generated by Django 2.0.3 on 2018-03-25 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resolution', '0002_auto_20180325_1230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yourresolutions',
            old_name='career',
            new_name='res_categ',
        ),
        migrations.RenameField(
            model_name='yourresolutions',
            old_name='health',
            new_name='res_title',
        ),
        migrations.RenameField(
            model_name='yourresolutions',
            old_name='travel',
            new_name='res_year',
        ),
    ]
