# Generated by Django 2.0.3 on 2018-03-25 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resolution', '0003_auto_20180325_1303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yourresolutions',
            old_name='res_categ',
            new_name='resolution_category',
        ),
        migrations.RenameField(
            model_name='yourresolutions',
            old_name='res_title',
            new_name='resolution_title',
        ),
        migrations.RenameField(
            model_name='yourresolutions',
            old_name='res_year',
            new_name='resolution_year',
        ),
    ]
